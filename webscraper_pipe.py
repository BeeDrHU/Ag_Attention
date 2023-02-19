{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOaQVGoZKLbvomMYk1Klr+c",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    },
    "gpuClass": "standard"
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/BeeDrHU/Ag_Attention/blob/webscraper/webscraper_pipe.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Installing the necessary packages."
      ],
      "metadata": {
        "id": "td-61_m_MimO"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install bs4\n",
        "!pip install requests\n",
        "!pip install selenium"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 905
        },
        "id": "uX214UMpMO71",
        "outputId": "d72e079b-ef47-4fa5-d61c-6af96e0216ae"
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n",
            "Requirement already satisfied: bs4 in /usr/local/lib/python3.8/dist-packages (0.0.1)\n",
            "Requirement already satisfied: beautifulsoup4 in /usr/local/lib/python3.8/dist-packages (from bs4) (4.6.3)\n",
            "Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n",
            "Requirement already satisfied: requests in /usr/local/lib/python3.8/dist-packages (2.25.1)\n",
            "Requirement already satisfied: chardet<5,>=3.0.2 in /usr/local/lib/python3.8/dist-packages (from requests) (4.0.0)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.8/dist-packages (from requests) (2022.12.7)\n",
            "Requirement already satisfied: urllib3<1.27,>=1.21.1 in /usr/local/lib/python3.8/dist-packages (from requests) (1.24.3)\n",
            "Requirement already satisfied: idna<3,>=2.5 in /usr/local/lib/python3.8/dist-packages (from requests) (2.10)\n",
            "Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n",
            "Collecting selenium\n",
            "  Downloading selenium-4.8.2-py3-none-any.whl (6.9 MB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m6.9/6.9 MB\u001b[0m \u001b[31m65.3 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: certifi>=2021.10.8 in /usr/local/lib/python3.8/dist-packages (from selenium) (2022.12.7)\n",
            "Collecting trio-websocket~=0.9\n",
            "  Downloading trio_websocket-0.9.2-py3-none-any.whl (16 kB)\n",
            "Collecting trio~=0.17\n",
            "  Downloading trio-0.22.0-py3-none-any.whl (384 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m384.9/384.9 KB\u001b[0m \u001b[31m35.9 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hCollecting urllib3[socks]~=1.26\n",
            "  Downloading urllib3-1.26.14-py2.py3-none-any.whl (140 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m140.6/140.6 KB\u001b[0m \u001b[31m17.2 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: attrs>=19.2.0 in /usr/local/lib/python3.8/dist-packages (from trio~=0.17->selenium) (22.2.0)\n",
            "Collecting outcome\n",
            "  Downloading outcome-1.2.0-py2.py3-none-any.whl (9.7 kB)\n",
            "Collecting sniffio\n",
            "  Downloading sniffio-1.3.0-py3-none-any.whl (10 kB)\n",
            "Collecting exceptiongroup>=1.0.0rc9\n",
            "  Downloading exceptiongroup-1.1.0-py3-none-any.whl (14 kB)\n",
            "Collecting async-generator>=1.9\n",
            "  Downloading async_generator-1.10-py3-none-any.whl (18 kB)\n",
            "Requirement already satisfied: sortedcontainers in /usr/local/lib/python3.8/dist-packages (from trio~=0.17->selenium) (2.4.0)\n",
            "Requirement already satisfied: idna in /usr/local/lib/python3.8/dist-packages (from trio~=0.17->selenium) (2.10)\n",
            "Collecting wsproto>=0.14\n",
            "  Downloading wsproto-1.2.0-py3-none-any.whl (24 kB)\n",
            "Requirement already satisfied: PySocks!=1.5.7,<2.0,>=1.5.6 in /usr/local/lib/python3.8/dist-packages (from urllib3[socks]~=1.26->selenium) (1.7.1)\n",
            "Collecting h11<1,>=0.9.0\n",
            "  Downloading h11-0.14.0-py3-none-any.whl (58 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m58.3/58.3 KB\u001b[0m \u001b[31m8.3 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hInstalling collected packages: urllib3, sniffio, outcome, h11, exceptiongroup, async-generator, wsproto, trio, trio-websocket, selenium\n",
            "  Attempting uninstall: urllib3\n",
            "    Found existing installation: urllib3 1.24.3\n",
            "    Uninstalling urllib3-1.24.3:\n",
            "      Successfully uninstalled urllib3-1.24.3\n",
            "Successfully installed async-generator-1.10 exceptiongroup-1.1.0 h11-0.14.0 outcome-1.2.0 selenium-4.8.2 sniffio-1.3.0 trio-0.22.0 trio-websocket-0.9.2 urllib3-1.26.14 wsproto-1.2.0\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "application/vnd.colab-display-data+json": {
              "pip_warning": {
                "packages": [
                  "urllib3"
                ]
              }
            }
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Defining the Website and Parsing the XML"
      ],
      "metadata": {
        "id": "lmNj5RESM55n"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def cook_soup_from_url(url, parser='lxml',sleep_time=0):\n",
        "    \"\"\"Uses requests to retreive webpage and returns a BeautifulSoup made using lxml parser.\"\"\"\n",
        "    import requests\n",
        "    from time import sleep\n",
        "    from bs4 import BeautifulSoup\n",
        "    \n",
        "    sleep(sleep_time)\n",
        "    response = requests.get(url)\n",
        "    \n",
        "    # check status of request\n",
        "    if response.status_code != 200:\n",
        "        raise Exception(f'Error: Status_code !=200.\\n status_code={response.status_code}')\n",
        "                        \n",
        "    c = response.content\n",
        "    # feed content into a beautiful soup using lxml\n",
        "    soup = BeautifulSoup(c,'lxml')\n",
        "    return soup"
      ],
      "metadata": {
        "id": "wuOJ4J_kNYsX"
      },
      "execution_count": 7,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Getting all Link Tags out of the Soup"
      ],
      "metadata": {
        "id": "p9UY5WX2NlNT"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def get_all_links(soup):#,attr_kwds=None):\n",
        "    \"\"\"Finds all links inside of soup that have the attributes(attr_kwds),which will be used in soup.findAll(attrs=attr_kwds).\n",
        "    Returns a list of links.\n",
        "    tag_type = 'a' or 'href'\"\"\"\n",
        "    all_a_tags = soup.findAll('a',attrs=kwds) \n",
        "    link_list = []\n",
        "    for link in all_a_tags:\n",
        "        test_link = link.get('href')#,attr=kwds)\n",
        "#         test_link = link.get('href',attrs=kwds)\n",
        "        link_list.append(test_link)\n",
        "    return link_list"
      ],
      "metadata": {
        "id": "6qmVfu0ENtPz"
      },
      "execution_count": 8,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Finalize the Links"
      ],
      "metadata": {
        "id": "8zWz_XkWNweq"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def make_absolute_links(source_url, rel_link_list):\n",
        "    \"\"\"Accepts the source_url for the source page of the rel_link_list and uses urljoin to return a list of valid absolute links.\"\"\"\n",
        "    \n",
        "    from urllib.parse import urlparse, urljoin\n",
        "\n",
        "    absolute_links=[]\n",
        "\n",
        "    # Create a for loop to loop through links and make absolute html paths\n",
        "    for link in rel_link_list:\n",
        "\n",
        "        # Get base url using a url pasers and the story_url at the beginning of the nb\n",
        "        abs_link = urljoin(source_url,link)    \n",
        "\n",
        "        #concatenate and append to a list \n",
        "        absolute_links.append(abs_link)\n",
        "    \n",
        "    return absolute_links"
      ],
      "metadata": {
        "id": "zSasFQW_N5p3"
      },
      "execution_count": 9,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Extract the Dictonary"
      ],
      "metadata": {
        "id": "0VE3QLVXN68Y"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def cook_batch_of_soups(link_list, sleep_time=1): #,user_fun = extract_target_text):\n",
        "    \"\"\"Accepts a list of links to extract and save in a list of dictionaries of soups\n",
        "    with their relative url path as their key.\n",
        "    Set user_fun to None to just extract full soups without user_extract\"\"\"\n",
        "    from time import sleep\n",
        "    from urllib.parse import urlparse, urljoin\n",
        "\n",
        "    batch_of_soups = []\n",
        "    \n",
        "    for link in link_list:\n",
        "        soup_dict = {}\n",
        "        \n",
        "        \n",
        "        # turn the url path into the dictionary key/title\n",
        "        url_dict_key_path = urlparse(link).path\n",
        "        url_dict_key = url_dict_key_path.split('/')[-1]\n",
        "        \n",
        "        soup_dict['_url'] = link\n",
        "        soup_dict['path'] = url_dict_key\n",
        "\n",
        "        # make a soup from the current link\n",
        "        page_soup = cook_soup_from_url(link, sleep_time=sleep_time)\n",
        "        soup_dict['soup'] = page_soup\n",
        "\n",
        "        \n",
        "#         if user_fun!=None:\n",
        "#             ## ADDING USER-SPECIFIED EXTRACTION FUNCTION       \n",
        "#             user_output = user_fun(page_soup) #can add inputs to function\n",
        "#             soup_dict['user_extract'] = user_output\n",
        "        \n",
        "        # Add current page's soup to batch_of_soups list\n",
        "        batch_of_soups.append(soup_dict)\n",
        "        \n",
        "    return batch_of_soups\n",
        "\n",
        "\n",
        "def extract_target_text(soup_or_tag,tag_name='p', attrs_dict=None, join_text =True, save_files=False):\n",
        "    \"\"\"User-specified function to add extraction of specific content during 'cook batch of soups'\"\"\"\n",
        "    \n",
        "    if attrs_dict==None:\n",
        "        found_tags = soup_or_tag.find_all(name=tag_name)\n",
        "    else:\n",
        "        found_tags = soup_or_tag.find_all(name=tag_name,attrs=attrs_dict)\n",
        "    \n",
        "    \n",
        "    # if extracting from multiple tags\n",
        "    output=[]\n",
        "    output = [tag.text for tag in found_tags if tag.text is not None]\n",
        "    \n",
        "    if join_text == True:\n",
        "        output = ' '.join(output)\n",
        "\n",
        "    ## ADDING SAVING EACH \n",
        "    if save_files==True:\n",
        "        text = output #soup.body.string\n",
        "        filename =f\"drive/My Drive/text_extract_{url_dict_key}.txt\"\n",
        "        soup_dict['filename'] = filename\n",
        "        with open(filename,'w+') as f:\n",
        "            f.write(text)\n",
        "        print(f'File  successfully saved as {filename}')\n",
        "\n",
        "    return  output"
      ],
      "metadata": {
        "id": "LEd7KV5qONxh"
      },
      "execution_count": 10,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Saving the Soup for Later"
      ],
      "metadata": {
        "id": "0G3uESUKOU0a"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def pickled_soup(soups, save_location='./', pickle_name='exported_soups.pckl'):\n",
        "    import pickle\n",
        "    import sys\n",
        "    \n",
        "    filepath = save_location+pickle_name\n",
        "    \n",
        "    with open(filepath,'wb') as f:\n",
        "        pickle.dump(soups, f)\n",
        "        \n",
        "    return print(f'Soup successfully pickled. Stored as {filepath}.')\n",
        "\n",
        "def load_leftovers(filepath):\n",
        "    import pickle\n",
        "    \n",
        "    print(f'Opening leftovers: {filepath}')\n",
        "    \n",
        "    with open(filepath, 'rb') as f:\n",
        "        leftover_soup = pickle.load(f)\n",
        "        \n",
        "    return leftover_soup"
      ],
      "metadata": {
        "id": "Y76kU5XHOXzS"
      },
      "execution_count": 11,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Using the Functions on a Website"
      ],
      "metadata": {
        "id": "JOdGFxNQOYpT"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import requests\n",
        "from bs4 import BeautifulSoup\n",
        "from urllib.parse import urlparse, urljoin\n",
        "\n",
        "url = 'https://en.wikipedia.org/wiki/Stock_market'\n",
        "soup = cook_soup_from_url(url,sleep_time=1)\n",
        "\n",
        "\n",
        "## Get all links that match are interal wikipedia redirects [yes?]\n",
        "kwds = {'class':'mw-redirect'}\n",
        "links = get_all_links(soup)#,kwds)\n",
        "\n",
        "\n",
        "# preview first 5 links\n",
        "print(links[:5])\n",
        "\n",
        "\n",
        "# Turn relative links into absolute links\n",
        "abs_links = make_absolute_links(url,links)\n",
        "print(abs_links[:5])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "mOHbOJSLO3Im",
        "outputId": "6d7b9fc9-c640-4e50-8a1e-c49929567cc0"
      },
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['/wiki/Collateralised_debt_obligation', '/wiki/Mortgage', '/wiki/Performance_bonds', '/wiki/Corporate_tax_haven', '/wiki/Credit_(finance)']\n",
            "['https://en.wikipedia.org/wiki/Collateralised_debt_obligation', 'https://en.wikipedia.org/wiki/Mortgage', 'https://en.wikipedia.org/wiki/Performance_bonds', 'https://en.wikipedia.org/wiki/Corporate_tax_haven', 'https://en.wikipedia.org/wiki/Credit_(finance)']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Selecting only the first 5 links to test\n",
        "abs_links_for_soups = abs_links[:5]\n",
        "\n",
        "\n",
        "# Cooking a batch of soups from those chosen links\n",
        "batch_of_soups = cook_batch_of_soups(abs_links_for_soups, sleep_time=2)\n",
        "\n",
        "# batch_of_soups is a list as long as the input link_list\n",
        "print(f'# of input links: == # of soups in batch:\\n{len(abs_links_for_soups)} == {len(batch_of_soups)}\\n')\n",
        "\n",
        "# batch_of_soups is a list of soup-dictionaries\n",
        "soup_dict = batch_of_soups[0]\n",
        "print('Each soup_dict has ',soup_dict.keys())\n",
        "\n",
        "# the page's soup is stored under soup_dict['soup']\n",
        "soup_from_soup_dict = soup_dict['soup']\n",
        "type(soup_from_soup_dict)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "F1S8WqqqPaeG",
        "outputId": "e7a47e6d-93e8-49cb-c821-7d66d557996a"
      },
      "execution_count": 14,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "# of input links: == # of soups in batch:\n",
            "5 == 5\n",
            "\n",
            "Each soup_dict has  dict_keys(['_url', 'path', 'soup'])\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "bs4.BeautifulSoup"
            ]
          },
          "metadata": {},
          "execution_count": 14
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Notes on extracting content.\n",
        "Edit the extract_target_text function in the James' functions settings or uncomment and use the extract_target_text_custom function below"
      ],
      "metadata": {
        "id": "qOJf6oynPinq"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "## ADDING extract_target_text to precisely target text\n",
        "# def extract_target_text_custom(soup_or_tag,tag_name='p', attrs_dict=None, join_text =True, save_files=False):\n",
        "#     \"\"\"User-specified function to add extraction of specific content during 'cook batch of soups'\"\"\"\n",
        "    \n",
        "#     if attrs_dict==None:\n",
        "#         found_tags = soup_or_tag.find_all(name=tag_name)\n",
        "#     else:\n",
        "#         found_tags = soup_or_tag.find_all(name=tag_name,attrs=attrs_dict)\n",
        "    \n",
        "    \n",
        "#     # if extracting from multiple tags\n",
        "#     output=[]\n",
        "#     output = [tag.text for tag in found_tags if tag.text is not None]\n",
        "    \n",
        "#     if join_text == True:\n",
        "#         output = ' '.join(output)\n",
        "\n",
        "#     ## ADDING SAVING EACH \n",
        "#     if save_files==True:\n",
        "#         text = output #soup.body.string\n",
        "#         filename =f\"drive/My Drive/text_extract_{url_dict_key}.txt\"\n",
        "#         soup_dict['filename'] = filename\n",
        "#         with open(filename,'w+') as f:\n",
        "#             f.write(text)\n",
        "#         print(f'File  successfully saved as {filename}')\n",
        "\n",
        "#     return  output\n",
        "\n",
        "# ####################\n",
        "\n",
        "## RUN A LOOP TO ADD EXTRACTED TEXT TO EACH SOUP IN THE BATCH\n",
        "for i, soup_dict in enumerate(batch_of_soups):\n",
        "    \n",
        "    # Get the soup from the dict\n",
        "    soup = soup_dict['soup']\n",
        "    \n",
        "    # Extract text \n",
        "    extracted_text = extract_target_text(soup)\n",
        "    \n",
        "    # Add key:value for results of extract\n",
        "    soup_dict['extracted'] = extracted_text\n",
        "    \n",
        "    # Replace the old soup_dict with the new one with 'extracted'\n",
        "    batch_of_soups[i] = soup_dict\n",
        "    \n",
        "example_extracted_text=batch_of_soups[0]['extracted']\n",
        "print(example_extracted_text[:1000])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "6U8OqEa9PmsN",
        "outputId": "5209e71c-31ac-4491-b55d-84e4bf91b358"
      },
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "A collateralized debt obligation (CDO) is a type of structured asset-backed security (ABS).[1] Originally developed as instruments for the corporate debt markets, after 2002 CDOs became vehicles for refinancing mortgage-backed securities (MBS).[2][3] Like other private label securities backed by assets, a CDO can be thought of as a promise to pay investors in a prescribed sequence, based on the cash flow the CDO collects from the pool of bonds or other assets it owns.[4] Distinctively, CDO credit risk is typically assessed based on a probability of default (PD) derived from ratings on those bonds or assets.[5]\n",
            " The CDO is \"sliced\" into sections known as \"tranches\", which \"catch\" the cash flow of interest and principal payments in sequence based on seniority.[6] If some loans default and the cash collected by the CDO is insufficient to pay all of its investors, those in the lowest, most \"junior\" tranches suffer losses first.[7] The last to lose payment from default are the safest, most \n"
          ]
        }
      ]
    }
  ]
}