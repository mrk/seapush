from ableton.v2.control_surface import Skin
from .colors import Basic, Rgb, Pulse, Blink, BiLed

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
        NoteNotScale = Rgb.BLACK
        NoteInvalid = Rgb.BLACK
        Feedback = Rgb.LIME
        FeedbackRecord = Rgb.RED.shade(1)
        NoteAction = Rgb.DARK_GREY

    class Recording:
        On = Basic.FULL
        Off = Basic.HALF
        Transition = Basic.FULL_BLINK_FAST
        FixedLengthRecordingOn = BiLed.YELLOW
        FixedLengthRecordingOff = BiLed.OFF

    class Automation:
        On = Basic.FULL
        Off = Basic.HALF

    class Session:
        Scene = BiLed.GREEN
        SceneTriggered = BiLed.GREEN_BLINK_FAST
        NoScene = BiLed.OFF
        ClipStopped = Rgb.AMBER
        ClipStarted = Pulse(Rgb.GREEN.shade(1), Rgb.GREEN, 48)
        ClipRecording = Pulse(Rgb.BLACK, Rgb.RED, 48)
        ClipTriggeredPlay = Blink(Rgb.GREEN, Rgb.BLACK, 24)
        ClipTriggeredRecord = Blink(Rgb.RED, Rgb.BLACK, 24)
        ClipEmpty = Rgb.BLACK
        RecordButton = Rgb.RED.shade(2)
        StopClip = Rgb.RED
        StopClipTriggered = Blink(Rgb.RED, Rgb.BLACK, 24)
        StoppedClip = Rgb.DARK_GREY

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
        PadAction = Rgb.RED
        
    class SlicedSimpler:
        SliceSelected = Rgb.OCEAN
        SliceUnselected = Rgb.YELLOW
        NoSlice = Rgb.YELLOW.shade(2)

    class LoopSelector:
        Playhead = Rgb.MAGENTA
        PlayheadRecord = Rgb.RED
        SelectedPage = Rgb.OCEAN
        InsideLoopStartBar = Rgb.SKY.highlight()
        InsideLoop = Rgb.SPRING.shade(1)
        OutsideLoop = Rgb.SPRING.shade(2)

    class NoteEditor:

        class Step:
            Low = Rgb.LIME.highlight()
            High = Rgb.LIME
            Full = Rgb.GREEN
            Muted = Rgb.AMBER.shade(2)

        class StepEditing:
            Low = Rgb.LIME.highlight()
            High = Rgb.LIME
            Full = Rgb.GREEN
            Muted = Rgb.AMBER.shade(2)

        StepSelected = Rgb.WHITE
        StepEmpty = Rgb.TURQUOISE.shade(2)
        StepDisabled = Rgb.RED.shade(2)
        Playhead = Rgb.MAGENTA
        PlayheadRecord = Rgb.RED
        QuantizationSelected = BiLed.GREEN
        QuantizationUnselected = BiLed.YELLOW
        NoteBase = Rgb.AMBER.shade(2)
        NoteScale = Rgb.DARK_GREY
        NoteNotScale = Rgb.BLACK
        NoteInvalid = Rgb.RED.shade(2)

    class Melodic:
        Playhead = Rgb.TURQUOISE.shade(2)
        PlayheadRecord = Rgb.RED.shade(1)

    class NoteRepeat:
        RateSelected = BiLed.RED
        RateUnselected = BiLed.YELLOW

    class Mixer:
        SoloOn = Rgb.OCEAN
        SoloOff = Rgb.OCEAN.shade(2)
        MuteOn = Rgb.DARK_GREY
        MuteOff = BiLed.YELLOW
        ArmSelected = BiLed.RED
        ArmUnselected = BiLed.RED_HALF

    class Browser:
        Load = BiLed.GREEN
        LoadNext = BiLed.YELLOW
        LoadNotPossible = BiLed.OFF
        Loading = BiLed.OFF
        Prehear = Rgb.BLUE
        PrehearOff = Rgb.WHITE

    class MessageBox:
        Cancel = BiLed.GREEN

    class Transport:
        PlayOn = Basic.FULL
        PlayOff = Basic.HALF

    class Metronome:
        On = Basic.FULL_BLINK_SLOW
        Off = Basic.FULL

    class FixedLength:
        On = Basic.FULL
        Off = Basic.HALF

    class Accent:
        On = Basic.FULL
        Off = Basic.HALF


def make_default_skin():
    return Skin(Colors)