# plot2vid

_The easiest way to create animations using plots._

This small Python package lets you store seperate matplotlib plots to create a video.

## Installation

```
pip install plot2vid
```

## Basic Usage

```python
from plot2vid import PlotRecorder
import matplotlib.pyplot as plt

# Setup
recorder = PlotRecorder("out.mp4")
fig = plt.figure()

for i in range(90):
    # Setting the plot limits
    plt.xlim(0,100)
    plt.ylim(0,100)

    # Plotting
    plt.scatter([i], [i])

    # Recording the frame
    recorder.add(fig)

    # Clearing the plot
    plt.clf()

# Storing the result
recorder.close()
```
The above code creates this video.

![ezgif-5-c21b239e33](https://github.com/fszewczyk/plot2vid/assets/60960225/5c7388aa-d955-46ff-b588-7bec7a4794b3)


## Advanced Usage

You can change the different settings of the recorder.

```python
recorder = plot2vid.PlotRecorder("out.mp4", fps=20)
```

## Roadmap

- [x] Support MP4
- [ ] Support AVI
- [x] Variable FPS
