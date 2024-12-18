interface SearchSpeedCorrection {
    speed: number
    correction: number
}

interface SearchSweepWidthVisibilityData {
    sw: number
    vis: number
}

interface SearchSpeedCorrections {
    Aircraft: SearchSpeedCorrection[]
    Helicopter: SearchSpeedCorrection[]
}

interface SearchHeightSweepWidths {
    [altitude: string]: SearchSweepWidthVisibilityData[]
}

interface SearchTargetSweepWidthData {
    weather_corrections: string
    speed_corrections: SearchSpeedCorrections
    Helicopter: SearchHeightSweepWidths
    Aircraft: SearchHeightSweepWidths
    Boat: SearchHeightSweepWidths
}

interface MarineSweepWidthData {
    [object_type: string]: SearchTargetSweepWidthData
}

export { MarineSweepWidthData, SearchTargetSweepWidthData, SearchHeightSweepWidths, SearchSpeedCorrections, SearchSweepWidthVisibilityData, SearchSpeedCorrection }