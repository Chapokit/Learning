def calculate_distance(v, a, t):
    return v*t + 0.5 * a * t **2



dist, velo, acc, duration = 0, 2, 0.5, 60
ans = calculate_distance(t=duration, v= velo, a =acc)