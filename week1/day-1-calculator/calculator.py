{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/jit0341/python-to-freelance-2025/blob/main/project_01_calculator.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 26,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 408
        },
        "id": "HcYxvVs4p9q0",
        "outputId": "dfd209e3-377a-4361-e46b-7a512bc5d7cc"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Result: 6\n",
            "Enter first number:2\n"
          ]
        },
        {
          "output_type": "error",
          "ename": "KeyboardInterrupt",
          "evalue": "Interrupted by user",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
            "\u001b[0;32m/tmp/ipython-input-1023383588.py\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     14\u001b[0m \u001b[0;32mwhile\u001b[0m \u001b[0;32mTrue\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     15\u001b[0m   \u001b[0ma\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0minput\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Enter first number:\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 16\u001b[0;31m   \u001b[0mb\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0minput\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Enter second number:\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     17\u001b[0m   \u001b[0moperation\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0minput\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Enter operation(+, -, *, /): \"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     18\u001b[0m   \u001b[0;32mif\u001b[0m \u001b[0moperation\u001b[0m \u001b[0;34m==\u001b[0m \u001b[0;34m\"+\"\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.12/dist-packages/ipykernel/kernelbase.py\u001b[0m in \u001b[0;36mraw_input\u001b[0;34m(self, prompt)\u001b[0m\n\u001b[1;32m   1175\u001b[0m                 \u001b[0;34m\"raw_input was called, but this frontend does not support input requests.\"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1176\u001b[0m             )\n\u001b[0;32m-> 1177\u001b[0;31m         return self._input_request(\n\u001b[0m\u001b[1;32m   1178\u001b[0m             \u001b[0mstr\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mprompt\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1179\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_parent_ident\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"shell\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.12/dist-packages/ipykernel/kernelbase.py\u001b[0m in \u001b[0;36m_input_request\u001b[0;34m(self, prompt, ident, parent, password)\u001b[0m\n\u001b[1;32m   1217\u001b[0m             \u001b[0;32mexcept\u001b[0m \u001b[0mKeyboardInterrupt\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1218\u001b[0m                 \u001b[0;31m# re-raise KeyboardInterrupt, to truncate traceback\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 1219\u001b[0;31m                 \u001b[0;32mraise\u001b[0m \u001b[0mKeyboardInterrupt\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Interrupted by user\"\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   1220\u001b[0m             \u001b[0;32mexcept\u001b[0m \u001b[0mException\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1221\u001b[0m                 \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mlog\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mwarning\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Invalid Message:\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mexc_info\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mTrue\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mKeyboardInterrupt\u001b[0m: Interrupted by user"
          ]
        }
      ],
      "source": [
        "\n",
        "def add(a,b):\n",
        "  return a + b\n",
        "def subtract(a,b):\n",
        "  return a - b\n",
        "def multiply(a,b):\n",
        "  return a * b\n",
        "def divide(a,b):\n",
        "  if b == 0:\n",
        "    return \"Error: can not divide by zero!\"\n",
        "  return a / b\n",
        "\n",
        "\n",
        "\n",
        "while True:\n",
        "  a = int(input(\"Enter first number:\"))\n",
        "  b = int(input(\"Enter second number:\"))\n",
        "  operation = input(\"Enter operation(+, -, *, /): \")\n",
        "  if operation == \"+\":\n",
        "        result = add(a,b)\n",
        "        print(f\"Result: {result}\")\n",
        "\n",
        "  elif operation == \"-\":\n",
        "        result = subtract(a,b)\n",
        "        print(f\"Result: {result}\")\n",
        "\n",
        "  elif operation == \"*\":\n",
        "        result = multiply(a,b)\n",
        "        print(f\"Result: {result}\")\n",
        "\n",
        "  elif operation == \"/\":\n",
        "        result = divide(a,b)\n",
        "        print(f\"Result: {result}\")\n",
        "\n",
        "  else:\n",
        "        print(\"Invalid operations!\")\n",
        "\n",
        "  continue_cal = input(\"Do another calculation? (yes/no):\")\n",
        "  if continue_cal == \"no\":\n",
        "         break\n",
        "\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "\"\"\"\n",
        "1. Lists: Write code to create a list of 5 fruits and print the 3rd fruit.\n",
        "2. Dictionary: Create a dictionary with 3 student names as keys and their ages as values. Print one student's age.\n",
        "3. For loop: Loop through numbers 1 to 5 and print each number.\n",
        "4. String method: Take a string \"  hello world  \" and remove the extra spaces, then make it uppercase.\n",
        "\n",
        "\"\"\"\n",
        "print(\"..... 1.List.....\")\n",
        "fruits = [\"apples\",\"mango\",\"orange\",\"Peach\",\"grapes\"]\n",
        "print(fruits[2])\n",
        "\n",
        "\n",
        "\n",
        "print(\"...3.Loop....\")\n",
        "for i in range(1,6):\n",
        "  print(i)\n",
        "\n",
        "print(\"....4.String....\")\n",
        "word = \"hello world\"\n",
        "word = word.strip().upper()\n",
        "\n",
        "print(word)\n",
        "\n",
        "print(\"....5.List comprehension....\") # 5. List comprehension: Create a list of squares of numbers from 1 to 5 using list comprehension.\n",
        "squares = [x **2 for x in range(1,6)]\n",
        "print(squares)\n",
        "\n",
        "students = {\"Ram\": 20, \"Sita\": 22, \"Arjun\": 19}\n",
        "print(students[\"Ram\"])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "myi1y60DL0aQ",
        "outputId": "86d2bdac-b637-4ca2-992e-d7cb5bd92106"
      },
      "execution_count": 68,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "..... 1.List.....\n",
            "orange\n",
            "...3.Loop....\n",
            "1\n",
            "2\n",
            "3\n",
            "4\n",
            "5\n",
            "....4.String....\n",
            "HELLO WORLD\n",
            "....5.List comprehension....\n",
            "[1, 4, 9, 16, 25]\n",
            "20\n"
          ]
        }
      ]
    }
  ],
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPMVdMvxedAcY7wXS3NMfW5",
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}