#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Date: 2024/10/11 17:20
Desc: 同花顺-财务指标-主要指标
https://basic.10jqka.com.cn/new/000063/finance.html
"""

import json

import pandas as pd
import requests
from bs4 import BeautifulSoup


def stock_financial_abstract_ths(
    symbol: str = "000063", indicator: str = "按报告期"
) -> pd.DataFrame:
    """
    同花顺-财务指标-主要指标
    https://basic.10jqka.com.cn/new/000063/finance.html
    :param symbol: 股票代码
    :type symbol: str
    :param indicator: 指标; choice of {"按报告期", "按年度", "按单季度"}
    :type indicator: str
    :return: 同花顺-财务指标-主要指标
    :rtype: pandas.DataFrame
    """
    url = f"https://basic.10jqka.com.cn/new/{symbol}/finance.html"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/89.0.4389.90 Safari/537.36",
    }
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, features="lxml")
    data_text = soup.find(name="p", attrs={"id": "main"}).string
    data_json = json.loads(data_text)
    df_index = [
        item[0] if isinstance(item, list) else item for item in data_json["title"]
    ]
    if indicator == "按报告期":
        temp_df = pd.DataFrame(
            data_json["report"][1:], columns=data_json["report"][0], index=df_index[1:]
        )
    elif indicator == "按单季度":
        temp_df = pd.DataFrame(
            data_json["simple"][1:], columns=data_json["simple"][0], index=df_index[1:]
        )
    else:
        temp_df = pd.DataFrame(
            data_json["year"][1:], columns=data_json["year"][0], index=df_index[1:]
        )
    temp_df = temp_df.T
    temp_df.reset_index(inplace=True)
    temp_df.rename(columns={"index": "报告期"}, inplace=True)
    return temp_df


def stock_financial_debt_ths(
    symbol: str = "000063", indicator: str = "按报告期"
) -> pd.DataFrame:
    """
    同花顺-财务指标-资产负债表
    https://basic.10jqka.com.cn/new/000063/finance.html
    https://basic.10jqka.com.cn/api/stock/finance/000063_debt.json
    :param symbol: 股票代码
    :type symbol: str
    :param indicator: 指标; choice of {"按报告期", "按年度"}
    :type indicator: str
    :return: 同花顺-财务指标-资产负债表
    :rtype: pandas.DataFrame
    """
    url = f"https://basic.10jqka.com.cn/api/stock/finance/{symbol}_debt.json"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/89.0.4389.90 Safari/537.36",
    }
    r = requests.get(url, headers=headers)
    data_json = json.loads(json.loads(r.text)["flashData"])
    df_index = [
        item[0] if isinstance(item, list) else item for item in data_json["title"]
    ]
    if indicator == "按报告期":
        temp_df = pd.DataFrame(
            data_json["report"][1:], columns=data_json["report"][0], index=df_index[1:]
        )
    else:
        temp_df = pd.DataFrame(
            data_json["year"][1:], columns=data_json["year"][0], index=df_index[1:]
        )
    temp_df = temp_df.T
    temp_df.reset_index(inplace=True)
    temp_df.rename(columns={"index": "报告期"}, inplace=True)
    return temp_df


def stock_financial_benefit_ths(
    symbol: str = "000063", indicator: str = "按报告期"
) -> pd.DataFrame:
    """
    同花顺-财务指标-利润表
    https://basic.10jqka.com.cn/new/000063/finance.html
    https://basic.10jqka.com.cn/api/stock/finance/000063_benefit.json
    :param symbol: 股票代码
    :type symbol: str
    :param indicator: 指标; choice of {"按报告期","按单季度", "按年度"}
    :type indicator: str
    :return: 同花顺-财务指标-利润表
    :rtype: pandas.DataFrame
    """
    url = f"https://basic.10jqka.com.cn/api/stock/finance/{symbol}_benefit.json"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/89.0.4389.90 Safari/537.36",
    }
    r = requests.get(url, headers=headers)
    data_json = json.loads(json.loads(r.text)["flashData"])
    df_index = [
        item[0] if isinstance(item, list) else item for item in data_json["title"]
    ]
    if indicator == "按报告期":
        temp_df = pd.DataFrame(
            data_json["report"][1:], columns=data_json["report"][0], index=df_index[1:]
        )
    elif indicator == "按单季度":
        temp_df = pd.DataFrame(
            data_json["simple"][1:], columns=data_json["simple"][0], index=df_index[1:]
        )
    else:
        temp_df = pd.DataFrame(
            data_json["year"][1:], columns=data_json["year"][0], index=df_index[1:]
        )
    temp_df = temp_df.T
    temp_df.reset_index(inplace=True)
    temp_df.rename(columns={"index": "报告期"}, inplace=True)
    return temp_df


def stock_financial_cash_ths(
    symbol: str = "000063", indicator: str = "按报告期"
) -> pd.DataFrame:
    """
    同花顺-财务指标-现金流量表
    https://basic.10jqka.com.cn/new/000063/finance.html
    https://basic.10jqka.com.cn/api/stock/finance/000063_cash.json
    :param symbol: 股票代码
    :type symbol: str
    :param indicator: 指标; choice of {"按报告期","按单季度", "按年度"}
    :type indicator: str
    :return: 同花顺-财务指标-现金流量表
    :rtype: pandas.DataFrame
    """
    url = f"https://basic.10jqka.com.cn/api/stock/finance/{symbol}_cash.json"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/89.0.4389.90 Safari/537.36",
    }
    r = requests.get(url, headers=headers)
    data_json = json.loads(json.loads(r.text)["flashData"])
    df_index = [
        item[0] if isinstance(item, list) else item for item in data_json["title"]
    ]
    if indicator == "按报告期":
        temp_df = pd.DataFrame(
            data_json["report"][1:], columns=data_json["report"][0], index=df_index[1:]
        )
    elif indicator == "按单季度":
        temp_df = pd.DataFrame(
            data_json["simple"][1:], columns=data_json["simple"][0], index=df_index[1:]
        )
    else:
        temp_df = pd.DataFrame(
            data_json["year"][1:], columns=data_json["year"][0], index=df_index[1:]
        )
    temp_df = temp_df.T
    temp_df.reset_index(inplace=True)
    temp_df.rename(columns={"index": "报告期"}, inplace=True)
    return temp_df


def stock_shareholder_change_ths(
    symbol: str = "688981"
) -> pd.DataFrame:
    """
    同花顺-公司大事-股东持股变动
    https://basic.10jqka.com.cn/new/688981/event.html
    :param symbol: 股票代码
    :type symbol: str
    :return: 同花顺-财务指标-主要指标
    :rtype: pandas.DataFrame
    """
    url = f"https://basic.10jqka.com.cn/new/{symbol}/event.html"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/109.0.0.0 Safari/537.36"
    }
    r = requests.get(url, headers=headers)
    r.encoding = 'gb2312'
    soup = BeautifulSoup(r.text, features="lxml")

    soup_find = soup.find("table", attrs={"class": "m_table data_table_1 m_hl"})

    if soup_find is not None:
        content_list = [item.text.strip() for item in soup_find]
        column_names = content_list[1].split("\n")
        row = content_list[3].replace("\t", "").replace("\n\n", "").replace("   ", "\n").replace(" ", "").replace("\n\n", "\n").split("\n")
        row = [item for item in row if item!=""]

        new_rows = []
        step = len(column_names)
        for i in range(0, len(row), step):
            new_rows.append(row[i : i + step])

        df = pd.DataFrame(new_rows, columns=column_names)

        return df
    return pd.DataFrame()


if __name__ == "__main__":
    stock_financial_abstract_ths_df = stock_financial_abstract_ths(
        symbol="000063", indicator="按报告期"
    )
    print(stock_financial_abstract_ths_df)

    stock_financial_abstract_ths_df = stock_financial_abstract_ths(
        symbol="000063", indicator="按年度"
    )
    print(stock_financial_abstract_ths_df)

    stock_financial_abstract_ths_df = stock_financial_abstract_ths(
        symbol="000063", indicator="按单季度"
    )
    print(stock_financial_abstract_ths_df)

    stock_financial_debt_ths_df = stock_financial_debt_ths(
        symbol="002004", indicator="按报告期"
    )
    print(stock_financial_debt_ths_df)

    stock_financial_debt_ths_df = stock_financial_debt_ths(
        symbol="000063", indicator="按年度"
    )
    print(stock_financial_debt_ths_df)

    stock_financial_benefit_ths_df = stock_financial_benefit_ths(
        symbol="000063", indicator="按报告期"
    )
    print(stock_financial_benefit_ths_df)

    stock_financial_benefit_ths_df = stock_financial_benefit_ths(
        symbol="000063", indicator="按年度"
    )
    print(stock_financial_benefit_ths_df)

    stock_financial_benefit_ths_df = stock_financial_benefit_ths(
        symbol="000063", indicator="按报告期"
    )
    print(stock_financial_benefit_ths_df)

    stock_financial_cash_ths_df = stock_financial_cash_ths(
        symbol="000063", indicator="按年度"
    )
    print(stock_financial_cash_ths_df)

    stock_financial_cash_ths_df = stock_financial_cash_ths(
        symbol="000063", indicator="按年度"
    )
    print(stock_financial_cash_ths_df)

    stock_financial_cash_ths_df = stock_financial_cash_ths(
        symbol="000063", indicator="按单季度"
    )
    print(stock_financial_cash_ths_df)

    stock_shareholder_change_ths_df = stock_shareholder_change_ths()
    print(stock_shareholder_change_ths_df)
