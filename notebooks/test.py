# %% [markdown]
# # Testing GitHub actions + papermill
# On this notebook, we are going to plot a noise linear function
# with the noise being a uniform distribution on the range
# [0, P], where P is a parametrized value

# %%
import numpy as np
import plotly.express as px

# %% {"tags": ["parameters"]}
param = 1.0

# %%
N = 1000
x = np.linspace(0, 10, N)
y = x + np.random.rand(N) * param

fig = px.scatter(x=x, y=y)
fig.show()
# %%
