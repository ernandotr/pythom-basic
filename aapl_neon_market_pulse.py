import yfinance as yf
import matplotlib.pyplot as plt, numpy as np

plt.style.use('dark_background')

p = yf.download("AAPL", period="3mo", progress=False)["Close"]

r=p.pct_change().fillna(0).values
x=np.arange(len(p))
plt.figure(figsize=(10,4))
sc=plt.scatter(x, p, c=r, cmap="plasma", s=45)
plt.plot(x, p, c="#ff00ff", alpha=0.6)

plt.title("AAPL Market Pulse", weight="bold")
plt.axis("off")
plt.colorbar(sc, label="Return Intensity")
plt.tight_layout()

