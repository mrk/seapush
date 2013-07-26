from Colors import Basic
from Colors import Rgb
from Colors import Pulse
from Colors import Blink
from Colors import BiLed
class Colors:
    class Option:
        Selected = BiLed.AMBER
        Unselected = BiLed.YELLOW_HALF
        On = BiLed.YELLOW
        Off = BiLed.OFF
        Unused = BiLed.OFF

    class List:
        ScrollerOn = BiLed.AMBER
        ScrollerOff = BiLed.AMBER_HALF

    class DefaultButton:
        On = Basic.FULL
        Off = Basic.HALF
        Disabled = Basic.OFF
        Alert = Basic.FULL_BLINK_SLOW

    class DefaultMatrix:
        On = Rgb.WHITE
        Off = Rgb.BLACK

    class Scales:
        Selected = BiLed.GREEN
        Unselected = BiLed.GREEN_HALF
        FixedOn = BiLed.AMBER
        FixedOff = BiLed.AMBER_HALF
        Diatonic = BiLed.AMBER
        Chromatic = BiLed.AMBER_HALF

    class Instrument:
        NoteBase = Rgb.ORCHID
        NoteScale = Rgb.TURQUOISE.shade(1)
        NoteForeign = Rgb.BLUE.shade(2)
        NoteInvalid = Rgb.BLACK
        NoteInactive = Rgb.BLACK
        NoteOff = Rgb.DARK_GREY
        Feedback = Rgb.LIME
        FeedbackRecord = Rgb.RED.shade(1)

    class Recording:
        On = Basic.FULL
        Off = Basic.HALF
        Transition = Basic.FULL_BLINK_FAST

    class Session:
        SceneSelected = BiLed.GREEN
        SceneUnselected = BiLed.OFF
        SceneTriggered = BiLed.GREEN_BLINK_FAST
        ClipStopped = Rgb.AMBER
        ClipStarted = Pulse(Rgb.GREEN.shade(1), Rgb.GREEN, 48)
        ClipRecording = Pulse(Rgb.BLACK, Rgb.RED, 48)
        ClipTriggeredPlay = Blink(Rgb.GREEN, Rgb.BLACK, 24)
        ClipTriggeredRecord = Blink(Rgb.RED, Rgb.BLACK, 24)
        ClipEmpty = Rgb.BLACK
        RecordButton = Rgb.RED.shade(2)

    class Zooming:
        Selected = Rgb.AMBER
        Stopped = Rgb.RED
        Playing = Rgb.GREEN
        Empty = Rgb.BLACK

    class TrackState:
        Common = Rgb.BLACK
        Stopped = Rgb.RED
        Disabled = Basic.OFF

    class DrumGroup:
        PadSelected = Rgb.MAGENTA
        PadSelectedNotSoloed = Rgb.MAGENTA.shade(1)
        PadFilled = Rgb.ORCHID.shade(1)
        PadEmpty = Rgb.BLUE.shade(2)
        PadMuted = Rgb.YELLOW.shade(1)
        PadMutedSelected = Rgb.AMBER
        PadSoloed = Rgb.OCEAN.highlight()
        PadSoloedSelected = Rgb.OCEAN
        PadInvisible = Rgb.BLACK

    class LoopSelector:
        Playhead = Rgb.MAGENTA
        PlayheadRecord = Rgb.RED
        SelectedPage = Rgb.OCEAN
        InsideLoop = Rgb.SPRING.shade(1)
        OutsideLoop = Rgb.SPRING.shade(2)

    class NoteEditor:
        Step = Rgb.LIME.highlight()
        StepHighVelocity = Rgb.LIME
        StepFullVelocity = Rgb.GREEN
        StepMuted = Rgb.AMBER.shade(2)
        StepEmpty = Rgb.TURQUOISE.shade(2)
        StepDisabled = Rgb.RED.shade(2)
        Playhead = Rgb.MAGENTA
        PlayheadRecord = Rgb.RED
        QuantizationSelected = BiLed.GREEN
        QuantizationUnselected = BiLed.YELLOW

    class NoteRepeat:
        RateSelected = BiLed.RED
        RateUnselected = BiLed.YELLOW

    class Mixer:
        SoloOn = Rgb.OCEAN
        SoloOff = Rgb.OCEAN.shade(2)
        MuteOn = Rgb.DARK_GREY
        MuteOff = BiLed.YELLOW
        StopTrack = Rgb.RED
        StoppingTrack = Blink(Rgb.RED, Rgb.BLACK, 24)
        ArmSelected = BiLed.RED
        ArmUnselected = BiLed.RED_HALF

    class Browser:
        Load = BiLed.GREEN
        LoadNext = BiLed.YELLOW
        LoadNotPossible = BiLed.OFF
        Loading = BiLed.OFF

    class MessageBox:
        Cancel = BiLed.GREEN
