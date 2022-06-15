import plotly.graph_objs as go
from random import randint


def collatz(n):
    list_steps = []
    while True:
        list_steps.append(n)
        if n % 2 == 0:
            n = n / 2
        elif n == 1:
            break
        else:
            n = 3 * n + 1
    return list_steps
 
        
n = randint(2, 1000000)
x = collatz(n)

fig = go.Figure()
fig.update_layout(title=dict(text=f'Collatz Conjecture. Number {n}, steps {len(x)}.', 
                             font=dict(size=20)), margin=dict(l=0, t=30, b=0, r=0))

fig.add_trace(go.Scatter(y=x, mode='lines', line=dict(width=3, color='black')))


fig.show()



