import numpy as np
import math
import sympy as sp


# Problem 1:
def calculate_buoyancy(V, density_fluid):
    """Calculates buoyant force exerted on object in water."""
    buoyancy = (
        str(density_fluid * V * 9.81) + "N"
    )  # now in (kg*m)/(s^2) - conversion to N is 1:1
    return buoyancy


# Problem 2:
def will_it_float(V, mass):
    if mass / V > 997:
        return True
    else:
        return False


# Problem 3:
def calculate_pressure(depth):
    return 1000 * 9.81 * depth


# Problem 4:
def calculate_acceleration(F, m):
    return F / m


# Problem 5:
def calc_ang_acceleration(tau, I):
    return tau / I


# Problem 6:
def calc_torque(F_mag, F_dir, r):
    return np.array([r * F_mag, F_dir])


# Problem 7:
def calc_mofinertia(m, r):
    return m * (r ^ 2)


# Problem 8:


def calculate_auv_acceleration(F_magnitude, F_angle):
    dir_acc = np.array(
        [(np.cos(F_angle) * F_magnitude) / 100, (np.sin(F_angle) * F_magnitude) / 100]
    )
    return np.linalg.norm(dir_acc)


def calculate_auv_angular_acceleration(F_magnitude, F_angle):
    return (0.5 * F_magnitude * np.sin(F_angle)) / 25


# Problem 9:
def calculate_auv2_acceleration(T, alpha, theta):
    dir_acc_local_frame = np.array(
        [
            (sp.cos(alpha) * T[0]) / 100
            + (sp.cos(-alpha) * T[1]) / 100
            + (sp.cos(sp.pi + alpha) * T[2]) / 100
            + (sp.cos(sp.pi - alpha) * T[3]) / 100,
            (sp.sin(alpha) * T[0]) / 100
            + (sp.sin(-alpha) * T[1]) / 100
            + (sp.sin(sp.pi + alpha) * T[2]) / 100
            + (sp.sin(sp.pi - alpha) * T[3]) / 100,
        ]
    )
    transformantion_matrix = np.array(
        [[sp.cos(theta), sp.sin(theta)], [-sp.sin(theta), sp.cos(theta)]]
    )
    dir_acc_global = np.dot(dir_acc_local_frame, transformantion_matrix)
    return dir_acc_global


def calculate_auv2_acceleration_m2(T, alpha, theta):
    dir_acc_local_frame = np.array(
        [
            (sp.cos(alpha + theta) * T[0]) / 100
            + (sp.cos(-alpha + theta) * T[1]) / 100
            + (sp.cos(sp.pi + alpha + theta) * T[2]) / 100
            + (sp.cos(sp.pi - alpha + theta) * T[3]) / 100,
            (sp.sin(alpha + theta) * T[0]) / 100
            + (sp.sin(-alpha + theta) * T[1]) / 100
            + (sp.sin(sp.pi + alpha + theta) * T[2]) / 100
            + (sp.sin(sp.pi - alpha + theta) * T[3]) / 100,
        ]
    )

    return dir_acc_local_frame


print(calculate_auv_acceleration(100, 0.5))

print(calculate_auv2_acceleration([4, 8, 0, 3], (5 * sp.pi) / 6, sp.pi / 8))
print(calculate_auv2_acceleration_m2([4, 8, 0, 3], (5 * sp.pi) / 6, sp.pi / 8))


def calculate_auv2_angular_acceleration(T, alpha, L):
    Tau1 = L * T[0] * sp.sin(alpha)
    Tau2 = L * T[1] * sp.sin(-alpha)
    Tau3 = L * T[2] * sp.sin(sp.pi + alpha)
    Tau4 = L * T[3] * sp.sin(sp.pi - alpha)
    I = 100 * (L ^ 2)
    netTau = Tau1 + Tau2 + Tau3 + Tau4
    return netTau / I
