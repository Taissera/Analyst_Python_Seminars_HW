# ДЗ. Задача 4. 
# Петя, Катя и Сережа делают из бумаги журавликов. 
# Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, 
# что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# 6 -> 1 4 1 
# 24 -> 4 16 4
# 60 -> 10 40 10

# S = Сережа + Катя + Петя
# Петя = Сережа
# Катя = (Сережа + Петя) * 2
# S = Сережа + 4*Сережа + Сережа
# S = 6*Сережа

S = int(input("Сколько журавликов сделали дети: "))
print(S//6, 4*(S//6), S//6)