# Adaptive Deep Reinforcement Learning Trading Agent

## The Problem
Financial markets change over time: sometimes trending upward (bullish), sometimes downward (bearish), sometimes moving sideways, and sometimes highly volatile. Most simple trading strategies fail to adapt to these changing conditions, performing well in one regime but badly in another. For example, a rule like “buy when the price is above the moving average” may work in upward trends but lose money in falling markets.

## The Aim
The aim of this project is to build a reinforcement learning agent that learns to trade by interacting with historical market data through trial and error. The agent should adapt its behaviour across different regimes — trending, sideways, and volatile — and be benchmarked against simple strategies such as Buy & Hold and moving average crossovers.

## What Will Count as Done
1. **A working agent**
   - The code runs end-to-end: from raw data to results.
   - The agent outputs trading decisions that are not random but learned from training.

2. **Evidence of performance**
   - Charts of portfolio growth versus Buy & Hold and moving average strategies.
   - Risk-adjusted performance metrics such as Sharpe ratio, maximum drawdown, and cumulative return.
   - Results compared across bullish, bearish, sideways, and volatile markets.

3. **Full documentation**
   - A clean, well-documented GitHub repository with clear code and structure.
   - Code that is written to a professional standard, with comments where appropriate.
   - A short report summarising methods, results, and lessons learned.
