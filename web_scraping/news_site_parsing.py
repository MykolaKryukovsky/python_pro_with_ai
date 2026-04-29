"""
Модуль для парсинга новостей и сохранения их в CSV.
"""
import asyncio
from datetime import datetime, timedelta

import aiohttp
import pandas as pd
import requests
from bs4 import BeautifulSoup


URL = "https://bbc.com/ukrainian"
DAYS_LIMIT = 7


async def get_page(session: aiohttp.ClientSession, url: str) -> BeautifulSoup|None:
    """Завантажує HTML-код сторінки та повертає BeautifulSoup-об'єкт."""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    try:
        async with session.get(url, headers=headers, timeout=10) as response:
            response.raise_for_status()
            html = await response.text()
            return BeautifulSoup(html, 'html.parser')
    except aiohttp.ClientError as e:
        print(f"Помилка при завантаженні сторінки: {e}")
        return None


def parse_news(soup: BeautifulSoup) -> list:
    """Витягує новини за тегами та атрибутами"""
    news_list = []
    if not soup:
        return news_list

    articles = soup.find_all(['div', 'article'], attrs={"role": "region"})

    if not articles:
        articles = soup.find_all('li')

    for article in articles:
        try:
            title_tag = article.find(['h2', 'h3'])
            if not title_tag:
                continue

            link_tag = article.find('a')
            title = title_tag.get_text(strip=True)
            link = link_tag['href'] if link_tag else "#"

            if not link.startswith('http'):
                link = "https://bbc.com" + link

            date_tag = article.find('time')
            date = date_tag.get_text(strip=True) if date_tag else "Дата не вказана"

            summary_tag = article.find('p')
            summary = summary_tag.get_text(strip=True) if summary_tag else "Опис відсутній"

            if title != "Без заголовка":
                news_list.append({
                    'title': title,
                    'link': link,
                    'date': date,
                    'summary': summary
                })
        except (AttributeError, TypeError):
            continue

    return news_list


def process_and_report(data: list, days: int) -> list|None:
    """
    Обробляє дані новин, фільтрує за датою та виводить статистику в консоль.
    """
    if not data:
        return None

    df = pd.DataFrame(data)

    df['date'] = (
        pd.to_datetime(df['date'], dayfirst=True, errors='coerce')
        .dt.tz_localize(None)
    )

    df = df.dropna(subset=['date'])

    cutoff_date = datetime.now() - timedelta(days=days)
    filtered_df = df[df['date'] >= cutoff_date].copy()

    print(f"\n--- Статистика новин за останні {days} днів ---")
    stats = filtered_df.groupby(filtered_df['date'].dt.date).size()
    if stats.empty:
        print("Новин за цей період не знайдено.")
    else:
        print(stats.to_string(header=False))
    print("-------------------------------------------\n")

    return filtered_df


def save_to_csv(df: pd.DataFrame, filename="news.csv") -> None:
    """
    Зберігає об'єкт DataFrame у файл CSV з підтримкою кирилиці.
    """
    if df is not None and not df.empty:
        df.to_csv(filename, index=False, encoding='utf-8-sig')
        print(f"Дані збережені у {filename}")
    else:
        print("Помилка при збереженні у CSV")


async def main():
    """Головна функція для запуску парсингу та обробки даних."""
    async with aiohttp.ClientSession() as session:
        print(f"Починаємо парсинг {URL}...")
        soup_obj = await get_page(session, URL)

        if soup_obj:
            raw_data = parse_news(soup_obj)
            print(f"Знайдено новин: {len(raw_data)}")

            processed_df = process_and_report(raw_data, DAYS_LIMIT)
            save_to_csv(processed_df)


if __name__ == "__main__":

    asyncio.run(main())
