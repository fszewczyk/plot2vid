# plot2vid

_The easiest way to create animations using plots._

This small Python package lets you store seperate matplotlib plots to create a video.

## Installation

```
pip install plot2vid
```

## Basic Usage

```python
from plot2vid import plot2vid

# Setup
recorder = plot2vid.PlotRecorder("out.mp4")
fig = plt.figure()

for i in range(90):
    # Setting the plot limits
    plt.xlim(0,10000)
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

## Advanced Usage

You can change different settings of the recorder.

```python
recorder = plot2vid.PlotRecorder("out.mp4", fps=20)
```

## Roadmap

- [x] Support MP4
- [ ] Support AVI
- [x] Variable FPS
