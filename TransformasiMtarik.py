import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider

# ================== DATA AWAL ==================
points = np.array([
    [1.0, 2.0],
    [3.0, 2.0],
    [3.0, 4.0],
    [1.0, 3.0]
])

mirror_y = 0.0  # Garis cermin
# ==============================================

def reflect_points(pts):
    reflected = pts.copy()
    reflected[:, 1] = 2 * mirror_y - reflected[:, 1]
    return reflected

# Setup figure
fig, ax = plt.subplots(figsize=(10, 8))
plt.subplots_adjust(left=0.1, bottom=0.35)

ax.set_xlim(-5, 10)
ax.set_ylim(-7, 7)
ax.set_aspect('equal')
ax.grid(True, alpha=0.3)
ax.axhline(y=mirror_y, color='red', linestyle='--', linewidth=2, label='Garis Cermin')

# Plot
obj_line, = ax.plot([], [], 'b-', linewidth=3, label='Objek Asli')
shadow_line, = ax.plot([], [], 'r--', linewidth=3, label='Bayangan')
obj_points = ax.scatter([], [], color='blue', s=100, zorder=5)
shadow_points = ax.scatter([], [], color='red', s=100, zorder=5)

ax.legend()
ax.set_title('Transformasi Cermin Interaktif - Geser Slider')

# Buat slider untuk setiap titik dan koordinat
sliders = []
positions = ['P1', 'P2', 'P3', 'P4']
coord = ['X', 'Y']

for i in range(4):
    for j in range(2):  # X dan Y
        ax_slider = plt.axes([0.15, 0.25 - (i*0.08 + j*0.04), 0.65, 0.03])
        s = Slider(ax_slider, f'{positions[i]} {coord[j]}', 
                   valmin=-6, valmax=10, valinit=points[i,j])
        sliders.append(s)

def update(val):
    # Ambil nilai dari semua slider
    new_points = np.zeros((4, 2))
    for i in range(4):
        for j in range(2):
            idx = i*2 + j
            new_points[i, j] = sliders[idx].val
    
    # Update objek
    x_obj = np.append(new_points[:,0], new_points[0,0])
    y_obj = np.append(new_points[:,1], new_points[0,1])
    obj_line.set_data(x_obj, y_obj)
    obj_points.set_offsets(new_points)
    
    # Update bayangan
    shadow = reflect_points(new_points)
    x_shad = np.append(shadow[:,0], shadow[0,0])
    y_shad = np.append(shadow[:,1], shadow[0,1])
    shadow_line.set_data(x_shad, y_shad)
    shadow_points.set_offsets(shadow)
    
    fig.canvas.draw_idle()

# Hubungkan slider ke fungsi update
for slider in sliders:
    slider.on_changed(update)

# Tampilkan awal
update(None)
plt.show()
