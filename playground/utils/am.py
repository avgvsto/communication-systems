import numpy


def amplitude_modulation(ac, am, fc, fm, time):

    # modulation index
    m = am / ac

    # AM formula terms
    carrier = ac * numpy.sin(2 * numpy.pi * fc * time)
    lower_sideband = m * ac / 2 * numpy.cos(2 * numpy.pi * (fc - fm) * time)
    upper_sideband = m * ac / 2 * numpy.cos(2 * numpy.pi * (fc + fm) * time)

    Sam = carrier + lower_sideband - upper_sideband

    return Sam
