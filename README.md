# Adaptive Deep Reinforcement Learning (DRL) Trading Agent

## The problem
The main problem is that financial markets don't stay the same. They change with time, sometimes trending upward (bullish), sometimes downward (bearish), sometimes crashing, or finally drift sideways. The markets can also be calm or incredibly volatile. The problem with this is that most of the simplest trading strategies don't adapt well when conditions change (bullish to bearish, low to high volatility, etc.), working in one regime but failing badly in another. An example of this is buying when the price is above the moving average.

## The aim
I aim to build a machine learning agent that will learn how to trade by interacting with historical market data through trial and error. It should be able to adapt its behaviour depending on whether the market is trending, crashing, or volatile.

It should be compared against simple benchmarks like ``Buy & Hold" or my other project which calculated Simple Moving Averages (SMAs), hopefully returning positive returns on theoretical investments.

## What will count as done
So there are a few checkpoints that I will compare my final project with to make sure that I have successfully implemented, which are:
1. A working agent
    - The code can be ran and the agent outputs a trading decision.
    - The output isn't random, and has learnt by training on market data.
    - The agent can run end-to-end, meaning that it is possible to press *run* and the whole program runs from raw data to results without having to run multiple pieces of code.
2. Evidence of performance
    - Clear charts should be produced showing the agents portfolio growth versus a Buy & Hold and SMA strategies growth.
    - Metrics such as the Sharpe ratio, Maximum Drawdown, and Cumulative return are calculated and displayed.
    - Performance across multiple different market conditions is considered (bullish, bearish, sideways, volatile).
3. Full documentation on GitHub
    - This project is not just for employability, its also to get myself used to using Git and its version control capabilities to the best of its abilites. Therefore, an end goal of this project is to have a clean, documented, well layed out GitHub repo that well reflects the best of my ability
    - The code that I write should be clean, well commented, and written to the best of my ability.
    - Another goal I would like to set myself, just as practice before I go into my 4th year and write my dissertation, is to write a short scientific report based on my findings from the project.
    
I am also setting a personal challenge to myself. It is becoming easier to use generative AI to write code, but I will be limiting myself to just use it as a form of enhanced search engine, only asking questions regarding misunderstandings or unknown methods from a library - instead of reading through hours worth of documentation. 