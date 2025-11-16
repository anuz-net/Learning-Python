import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

# Parametric heart
t = np.linspace(0, 2*np.pi, 1000)
x = 16*np.sin(t)**3
y = 13*np.cos(t) - 5*np.cos(2*t) - 2*np.cos(3*t) - np.cos(4*t)

# figure
fig, ax = plt.subplots(figsize=(6,6))
ax.set_aspect('equal')
ax.axis('off')

# compute limits with margin
xmargin = (x.max() - x.min()) * 0.1
ymargin = (y.max() - y.min()) * 0.1
ax.set_xlim(x.min() - xmargin, x.max() + xmargin)
ax.set_ylim(y.min() - ymargin, y.max() + ymargin)

# artists
line, = ax.plot([], [], color='red', linewidth=3)
# create the fill patch now (invisible initially) and keep reference
fill_patch = ax.fill([], [], color='pink', alpha=0.0)[0]
time_text = ax.text(0, 0, "", color='red', fontsize=16, fontweight='bold',
                    ha='center', va='center', alpha=0.0)

# animation parameters
draw_frames = len(x)              # frames to draw outline
fill_fade_frames = 30            # frames to fade fill in
text_fade_frames = 40            # frames to fade text in
total_frames = draw_frames + fill_fade_frames + text_fade_frames

def init():
    line.set_data([], [])
    fill_patch.set_xy(np.column_stack(([], [])))
    fill_patch.set_alpha(0.0)
    time_text.set_text("")
    time_text.set_alpha(0.0)
    return line, fill_patch, time_text

def update(frame):
    # 0 .. draw_frames-1 : draw the outline progressively
    if frame < draw_frames:
        idx = frame + 1  # include this point
        line.set_data(x[:idx], y[:idx])
        # keep the fill invisible until we start fading it
        fill_patch.set_alpha(0.0)
        time_text.set_alpha(0.0)
    # draw_frames .. draw_frames+fill_fade_frames-1 : show and fade-in fill
    elif frame < draw_frames + fill_fade_frames:
        line.set_data(x, y)  # outline complete
        # set path for fill (only needs to be set once, but safe here)
        fill_patch.set_xy(np.column_stack((x, y)))
        # fade alpha from 0 -> 0.6
        local = frame - draw_frames
        alpha = min((local + 1) / fill_fade_frames * 0.6, 0.6)
        fill_patch.set_alpha(alpha)
        time_text.set_alpha(0.0)
    # remaining frames: keep fill and fade text in
    else:
        line.set_data(x, y)
        fill_patch.set_xy(np.column_stack((x, y)))
        fill_patch.set_alpha(0.6)
        local = frame - (draw_frames + fill_fade_frames)
        alpha = min((local + 1) / text_fade_frames, 1.0)
        time_text.set_text("I Love You Prabin")
        time_text.set_alpha(alpha)

    # return all artists that changed (required for blit=True)
    return line, fill_patch, time_text

ani = FuncAnimation(fig, update, frames=total_frames, init_func=init,
                    blit=True, interval=10, repeat=False)

# Optional: save to GIF (uncomment to enable)
# writer = PillowWriter(fps=60)   # choose desired fps
# ani.save("heart_animation.gif", writer=writer)

plt.show()
