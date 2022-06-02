const marine_sweep_width_weather_corrections = {
    'small': {
        'IAMSAR': {
            'low': 1.0,
            'medium': 0.5,
            'high': 0.25,
        }
    },
    'large': {
        'IAMSAR': {
            'low': 1.0,
            'medium': 0.9,
            'high': 0.9,
        },
        /* This data is from the Australian National Search and Rescue Manual - 2022 Edition Version 1 */
        'au': {
            'low': 1.0,
            'medium': 0.8,
            'high': 0.5,
        },
    },
}

export { marine_sweep_width_weather_corrections };