{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "NIFTY50-01/01/20-18/10/20.ipynb",
      "provenance": [],
      "mount_file_id": "1lbDhIXVLCKDtTtJMSkFO5OF5GvDoz2F3",
      "authorship_tag": "ABX9TyOy+6U2TNEsGvAc1x/eyFGm",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/akshar99/COVID-19-EDA-Forecasting-using-fbProphet/blob/main/NIFTY50_01_01_20_18_10_20.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "nSfQRsCHozBN",
        "outputId": "6771ed2d-77df-4502-88b0-98a43a642b5a",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        }
      },
      "source": [
        "pd.__version__"
      ],
      "execution_count": 84,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            },
            "text/plain": [
              "'1.1.2'"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 84
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "MLcuYlMIX-hY"
      },
      "source": [
        "import pandas as pd\n",
        "import datetime\n",
        "import numpy as np"
      ],
      "execution_count": 69,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "IRF5q0V7Kj2T"
      },
      "source": [
        "df = pd.read_excel('/content/drive/My Drive/python/NSE 010120-181020.xlsx')"
      ],
      "execution_count": 19,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "NQ7xixSrM6cn",
        "outputId": "f1b0e11c-8931-42df-8e8e-ede572900f35",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 191
        }
      },
      "source": [
        "df.head()"
      ],
      "execution_count": 20,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Date</th>\n",
              "      <th>Open</th>\n",
              "      <th>High</th>\n",
              "      <th>Low</th>\n",
              "      <th>Close</th>\n",
              "      <th>Shares Traded</th>\n",
              "      <th>Turnover (Rs. Cr)</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>2020-01-01</td>\n",
              "      <td>12202.15</td>\n",
              "      <td>12222.20</td>\n",
              "      <td>12165.30</td>\n",
              "      <td>12182.50</td>\n",
              "      <td>304078039</td>\n",
              "      <td>10445.68</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>2020-01-02</td>\n",
              "      <td>12198.55</td>\n",
              "      <td>12289.90</td>\n",
              "      <td>12195.25</td>\n",
              "      <td>12282.20</td>\n",
              "      <td>407697594</td>\n",
              "      <td>15256.55</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>2020-01-03</td>\n",
              "      <td>12261.10</td>\n",
              "      <td>12265.60</td>\n",
              "      <td>12191.35</td>\n",
              "      <td>12226.65</td>\n",
              "      <td>428770054</td>\n",
              "      <td>16827.27</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>2020-01-04</td>\n",
              "      <td>12170.60</td>\n",
              "      <td>12179.10</td>\n",
              "      <td>11974.20</td>\n",
              "      <td>11993.05</td>\n",
              "      <td>396501419</td>\n",
              "      <td>16869.22</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>2020-01-05</td>\n",
              "      <td>12079.10</td>\n",
              "      <td>12152.15</td>\n",
              "      <td>12005.35</td>\n",
              "      <td>12052.95</td>\n",
              "      <td>447818617</td>\n",
              "      <td>17797.68</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "        Date      Open      High  ...     Close  Shares Traded  Turnover (Rs. Cr)\n",
              "0 2020-01-01  12202.15  12222.20  ...  12182.50      304078039           10445.68\n",
              "1 2020-01-02  12198.55  12289.90  ...  12282.20      407697594           15256.55\n",
              "2 2020-01-03  12261.10  12265.60  ...  12226.65      428770054           16827.27\n",
              "3 2020-01-04  12170.60  12179.10  ...  11993.05      396501419           16869.22\n",
              "4 2020-01-05  12079.10  12152.15  ...  12052.95      447818617           17797.68\n",
              "\n",
              "[5 rows x 7 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 20
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "TGa744DhNgHQ"
      },
      "source": [
        "df['Date'] = pd.to_datetime(df['Date'] , format='%Y-%m-%d')"
      ],
      "execution_count": 29,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ksXGfl1gZxeo"
      },
      "source": [
        "df['Date'] = pd.to_datetime(df['Date'] , format='%d-%m-%Y')"
      ],
      "execution_count": 33,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "3m1ZiZs-YTLu",
        "outputId": "73b7d7bc-77ca-4573-9c19-7ed5c48fbf9e",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 245
        }
      },
      "source": [
        "df.info()"
      ],
      "execution_count": 34,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 200 entries, 0 to 199\n",
            "Data columns (total 7 columns):\n",
            " #   Column             Non-Null Count  Dtype         \n",
            "---  ------             --------------  -----         \n",
            " 0   Date               200 non-null    datetime64[ns]\n",
            " 1   Open               200 non-null    float64       \n",
            " 2   High               200 non-null    float64       \n",
            " 3   Low                200 non-null    float64       \n",
            " 4   Close              200 non-null    float64       \n",
            " 5   Shares Traded      200 non-null    int64         \n",
            " 6   Turnover (Rs. Cr)  200 non-null    float64       \n",
            "dtypes: datetime64[ns](1), float64(5), int64(1)\n",
            "memory usage: 11.1 KB\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "dbGgUuygYVx9"
      },
      "source": [
        "Date = df['Date']"
      ],
      "execution_count": 35,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "S_6zC1_6Yw8i",
        "outputId": "dcce7684-e060-489b-8566-d8c411da2819",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 212
        }
      },
      "source": [
        "Date"
      ],
      "execution_count": 36,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0     2020-01-01\n",
              "1     2020-01-02\n",
              "2     2020-01-03\n",
              "3     2020-01-04\n",
              "4     2020-01-05\n",
              "         ...    \n",
              "195   2020-07-22\n",
              "196   2020-07-23\n",
              "197   2020-07-24\n",
              "198   2020-07-25\n",
              "199   2020-07-26\n",
              "Name: Date, Length: 200, dtype: datetime64[ns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 36
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "du02SMTrYzkv"
      },
      "source": [
        "from datetime import datetime"
      ],
      "execution_count": 27,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "styJcdYeZQRZ"
      },
      "source": [
        "#dateobject = []\n",
        "#for i in range(len(Date)):\n",
        " # dateobject[i] = datetime.strptime(Date[i] ,'%Y-%m-%d' )\n",
        "#  dateobject.append(dateobject[i])\n"
      ],
      "execution_count": 40,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "5x5I4k4YZhb6"
      },
      "source": [
        "df['Percentage Change'] = ((df['Open'] - df['Close'])/100).astype(float)"
      ],
      "execution_count": 60,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "oBwr7jDkb21Z",
        "outputId": "88d5e853-a711-4c45-df0d-5b744535ba50",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 212
        }
      },
      "source": [
        "df['Percentage Change']"
      ],
      "execution_count": 61,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0      0.1965\n",
              "1     -0.8365\n",
              "2      0.3445\n",
              "3      1.7755\n",
              "4      0.2615\n",
              "        ...  \n",
              "195    0.4260\n",
              "196    0.0015\n",
              "197   -0.5365\n",
              "198    3.4310\n",
              "199   -0.3505\n",
              "Name: Percentage Change, Length: 200, dtype: float64"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 61
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "VNFc4rh4lqgP"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "mdMeRGtqb5PH"
      },
      "source": [
        "df['Marker'] = np.nan"
      ],
      "execution_count": 70,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "xH8jtTDVcZo-"
      },
      "source": [
        "for i in range(len(df['Marker'])):\n",
        "  if df['Marker'][i] > 0:\n",
        "    df['Marker'][i].append('Profit')\n",
        "  elif df['Marker'][i] < 0:\n",
        "    df['Marker'][i].append('Loss')\n",
        "  elif df['Marker'][i] == 0:\n",
        "    df['Marker'][i].append('Flat')  "
      ],
      "execution_count": 71,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "S_2HUxOSm-iv",
        "outputId": "aaee8916-f4ec-4cec-d1fb-5b828ab29b82",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 272
        }
      },
      "source": [
        "pd.options.mode.changed_assignment = None"
      ],
      "execution_count": 79,
      "outputs": [
        {
          "output_type": "error",
          "ename": "OptionError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mOptionError\u001b[0m                               Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-79-8c5f67a8a94e>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mpd\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0moptions\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mmode\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mchanged_assignment\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;32m/usr/local/lib/python3.6/dist-packages/pandas/_config/config.py\u001b[0m in \u001b[0;36m__setattr__\u001b[0;34m(self, key, val)\u001b[0m\n\u001b[1;32m    196\u001b[0m             \u001b[0m_set_option\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mprefix\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mval\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    197\u001b[0m         \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 198\u001b[0;31m             \u001b[0;32mraise\u001b[0m \u001b[0mOptionError\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"You can only set the value of existing options\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    199\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    200\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0m__getattr__\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mkey\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0mstr\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mOptionError\u001b[0m: 'You can only set the value of existing options'"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "k5MfAvPqdH4Z",
        "outputId": "3a614923-f775-4d45-dfeb-d5ac724cf4d2",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 223
        }
      },
      "source": [
        "for i in range(len(df['Marker'])):\n",
        "  if df['Percentage Change'][i] > 0:\n",
        "    df['Marker'][i] =='Profit'\n",
        "  elif df['Percentage Change'][i] < 0:\n",
        "    df['Marker'][i] = 'Loss'\n",
        "  elif df['Percentage Change'][i] == 0:\n",
        "    df['Marker'][i] = 'Flat'  "
      ],
      "execution_count": 82,
      "outputs": [
        {
          "output_type": "error",
          "ename": "AttributeError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-82-e9145deac6fc>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0;32mfor\u001b[0m \u001b[0mi\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mrange\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mlen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mdf\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m'Marker'\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      2\u001b[0m   \u001b[0;32mif\u001b[0m \u001b[0mdf\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m'Percentage Change'\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mi\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m>\u001b[0m \u001b[0;36m0\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 3\u001b[0;31m     \u001b[0;34m(\u001b[0m\u001b[0mdf\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m'Marker'\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mi\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m==\u001b[0m\u001b[0;34m'Profit'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcopy\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mdeep\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mTrue\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      4\u001b[0m   \u001b[0;32melif\u001b[0m \u001b[0mdf\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m'Percentage Change'\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mi\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m<\u001b[0m \u001b[0;36m0\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m     \u001b[0;34m(\u001b[0m\u001b[0mdf\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m'Marker'\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mi\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m==\u001b[0m \u001b[0;34m'Loss'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcopy\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mdeep\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mTrue\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mAttributeError\u001b[0m: 'bool' object has no attribute 'copy'"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "W6mr8bPCjzzy",
        "outputId": "428ee2be-6059-48fa-8467-4fe9ccc4b801",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 212
        }
      },
      "source": [
        "df['Marker']"
      ],
      "execution_count": 78,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0       NaN\n",
              "1      Loss\n",
              "2       NaN\n",
              "3       NaN\n",
              "4       NaN\n",
              "       ... \n",
              "195     NaN\n",
              "196     NaN\n",
              "197    Loss\n",
              "198     NaN\n",
              "199    Loss\n",
              "Name: Marker, Length: 200, dtype: object"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 78
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "qQbpn4BPlyqw"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}