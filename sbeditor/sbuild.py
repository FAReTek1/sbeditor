from .sbeditor import *


class Motion:
    class MoveSteps(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "motion_movesteps", shadow=shadow, pos=pos)

        def set_steps(self, value, input_type: str | int = "number", shadow_status: int = 1, *,
                      input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("STEPS", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class TurnRight(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "motion_turnright", shadow=shadow, pos=pos)

        def set_degrees(self, value, input_type: str | int = "number", shadow_status: int = 1, *,
                        input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("DEGREES", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class TurnLeft(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "motion_turnleft", shadow=shadow, pos=pos)

        def set_degrees(self, value, input_type: str | int = "number", shadow_status: int = 1, *,
                        input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("DEGREES", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class GoTo(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "motion_goto", shadow=shadow, pos=pos)

        def set_to(self, value, input_type: str | int = "block", shadow_status: int = 1, *,
                   input_id: str = None, obscurer: str | Block = None):
            return self.add_input(Input("TO", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class GoToMenu(Block):
        def __init__(self, *, shadow: bool = True, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "motion_goto_menu", shadow=shadow, pos=pos)

        def set_to(self, value: str = "_random_", value_id: str = None):
            return self.add_field(Field("TO", value, value_id))

    class GoToXY(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "motion_gotoxy", shadow=shadow, pos=pos)

        def set_x(self, value, input_type: str | int = "number", shadow_status: int = 1, *,
                  input_id: str = None, obscurer: str | Block = None):
            return self.add_input(Input("X", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

        def set_y(self, value, input_type: str | int = "number", shadow_status: int = 1, *,
                  input_id: str = None, obscurer: str | Block = None):
            return self.add_input(Input("Y", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class GlideTo(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "motion_glideto", shadow=shadow, pos=pos)

        def set_secs(self, value, input_type: str | int = "positive number", shadow_status: int = 1, *,
                     input_id: str = None, obscurer: str | Block = None):
            return self.add_input(Input("SECS", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

        def set_to(self, value, input_type: str | int = "block", shadow_status: int = 1, *,
                   input_id: str = None, obscurer: str | Block = None):
            return self.add_input(Input("TO", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class GlideToMenu(Block):
        def __init__(self, *, shadow: bool = True, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "motion_glideto_menu", shadow=shadow, pos=pos)

        def set_to(self, value: str = "_random_", value_id: str = None):
            return self.add_field(Field("TO", value, value_id))

    class GlideSecsToXY(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "motion_glidesecstoxy", shadow=shadow, pos=pos)

        def set_x(self, value, input_type: str | int = "number", shadow_status: int = 1, *,
                  input_id: str = None, obscurer: str | Block = None):
            return self.add_input(Input("X", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

        def set_y(self, value, input_type: str | int = "number", shadow_status: int = 1, *,
                  input_id: str = None, obscurer: str | Block = None):
            return self.add_input(Input("Y", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

        def set_secs(self, value, input_type: str | int = "positive number", shadow_status: int = 1, *,
                     input_id: str = None, obscurer: str | Block = None):
            return self.add_input(Input("SECS", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class PointInDirection(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "motion_pointindirection", shadow=shadow, pos=pos)

        def set_direction(self, value, input_type: str | int = "angle", shadow_status: int = 1, *,
                          input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("DIRECTION", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class PointTowards(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "motion_pointtowards", shadow=shadow, pos=pos)

        def set_towards(self, value, input_type: str | int = "block", shadow_status: int = 1, *,
                        input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("TOWARDS", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class PointTowardsMenu(Block):
        def __init__(self, *, shadow: bool = True, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "motion_pointtowards_menu", shadow=shadow, pos=pos)

        def set_towards(self, value: str = "_mouse_", value_id: str = None):
            return self.add_field(Field("TOWARDS", value, value_id))

    class ChangeXBy(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "motion_changexby", shadow=shadow, pos=pos)

        def set_dx(self, value, input_type: str | int = "number", shadow_status: int = 1, *,
                   input_id: str = None, obscurer: str | Block = None):
            return self.add_input(Input("DX", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class ChangeYBy(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "motion_changeyby", shadow=shadow, pos=pos)

        def set_dy(self, value, input_type: str | int = "number", shadow_status: int = 1, *,
                   input_id: str = None, obscurer: str | Block = None):
            return self.add_input(Input("DY", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class SetX(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "motion_setx", shadow=shadow, pos=pos)

        def set_x(self, value, input_type: str | int = "number", shadow_status: int = 1, *,
                  input_id: str = None, obscurer: str | Block = None):
            return self.add_input(Input("X", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class SetY(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "motion_sety", shadow=shadow, pos=pos)

        def set_y(self, value, input_type: str | int = "number", shadow_status: int = 1, *,
                  input_id: str = None, obscurer: str | Block = None):
            return self.add_input(Input("Y", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class IfOnEdgeBounce(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "motion_ifonedgebounce", shadow=shadow, pos=pos)

    class SetRotationStyle(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "motion_setrotationstyle", shadow=shadow, pos=pos)

        def set_style(self, value: str = "all around", value_id: str = None):
            return self.add_field(Field("STYLE", value, value_id))

    class XPosition(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "motion_xposition", shadow=shadow, pos=pos)

    class YPosition(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "motion_yposition", shadow=shadow, pos=pos)

    class Direction(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "motion_direction", shadow=shadow, pos=pos)

    class ScrollRight(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "motion_scroll_right", shadow=shadow, pos=pos)

        def set_distance(self, value, input_type: str | int = "number", shadow_status: int = 1, *,
                         input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("DISTANCE", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class ScrollUp(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "motion_scroll_up", shadow=shadow, pos=pos)

        def set_distance(self, value, input_type: str | int = "number", shadow_status: int = 1, *,
                         input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("DISTANCE", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class AlignScene(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "motion_align_scene", shadow=shadow, pos=pos)

        def set_alignment(self, value: str = "bottom-left", value_id: str = None):
            return self.add_field(Field("ALIGNMENT", value, value_id))

    class XScroll(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "motion_xscroll", shadow=shadow, pos=pos)

    class YScroll(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "motion_yscroll", shadow=shadow, pos=pos)


class Looks:
    class SayForSecs(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "looks_sayforsecs", shadow=shadow, pos=pos)

        def set_message(self, value="Hello!", input_type: str | int = "string", shadow_status: int = 1, *,
                        input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("MESSAGE", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer)
            )

        def set_secs(self, value=2, input_type: str | int = "positive integer", shadow_status: int = 1, *,
                     input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("SECS", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer)
            )

    class Say(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "looks_say", shadow=shadow, pos=pos)

        def set_message(self, value="Hello!", input_type: str | int = "string", shadow_status: int = 1, *,
                        input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("MESSAGE", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer)
            )

    class ThinkForSecs(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "looks_thinkforsecs", shadow=shadow, pos=pos)

        def set_message(self, value="Hmm...", input_type: str | int = "string", shadow_status: int = 1, *,
                        input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("MESSAGE", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer)
            )

        def set_secs(self, value=2, input_type: str | int = "positive integer", shadow_status: int = 1, *,
                     input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("SECS", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer)
            )

    class Think(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "looks_think", shadow=shadow, pos=pos)

        def set_message(self, value="Hmm...", input_type: str | int = "string", shadow_status: int = 1, *,
                        input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("MESSAGE", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer)
            )

    class SwitchCostumeTo(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "looks_switchcostumeto", shadow=shadow, pos=pos)

        def set_costume(self, value, input_type: str | int = "block", shadow_status: int = 1, *,
                        input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("COSTUME", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class Costume(Block):
        def __init__(self, *, shadow: bool = True, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "looks_costume", shadow=shadow, pos=pos)

        def set_costume(self, value: str = "costume1", value_id: str = None):
            return self.add_field(Field("COSTUME", value, value_id))

    class NextCostume(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "looks_nextcostume", shadow=shadow, pos=pos)

    class SwitchBackdropTo(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "looks_switchbackdropto", shadow=shadow, pos=pos)

        def set_backdrop(self, value, input_type: str | int = "block", shadow_status: int = 1, *,
                         input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("BACKDROP", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class Backdrops(Block):
        def __init__(self, *, shadow: bool = True, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "looks_backdrops", shadow=shadow, pos=pos)

        def set_backdrop(self, value: str = "costume1", value_id: str = None):
            return self.add_field(Field("BACKDROP", value, value_id))

    class SwitchBackdropToAndWait(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "looks_switchbackdroptoandwait", shadow=shadow, pos=pos)

        def set_backdrop(self, value, input_type: str | int = "block", shadow_status: int = 1, *,
                         input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("BACKDROP", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class NextBackdrop(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "looks_nextbackdrop", shadow=shadow, pos=pos)

    class ChangeSizeBy(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "looks_changesizeby", shadow=shadow, pos=pos)

        def set_change(self, value="10", input_type: str | int = "number", shadow_status: int = 1, *,
                       input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("CHANGE", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class SetSizeTo(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "looks_setsizeto", shadow=shadow, pos=pos)

        def set_size(self, value="100", input_type: str | int = "number", shadow_status: int = 1, *,
                     input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("SIZE", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class ChangeEffectBy(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "looks_changeeffectby", shadow=shadow, pos=pos)

        def set_change(self, value="100", input_type: str | int = "number", shadow_status: int = 1, *,
                       input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("CHANGE", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

        def set_effect(self, value: str = "COLOR", value_id: str = None):
            return self.add_field(Field("EFFECT", value, value_id))

    class SetEffectTo(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "looks_seteffectto", shadow=shadow, pos=pos)

        def set_value(self, value="0", input_type: str | int = "number", shadow_status: int = 1, *,
                      input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("VALUE", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

        def set_effect(self, value: str = "COLOR", value_id: str = None):
            return self.add_field(Field("EFFECT", value, value_id))

    class ClearGraphicEffects(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "looks_cleargraphiceffects", shadow=shadow, pos=pos)

    class Hide(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "looks_hide", shadow=shadow, pos=pos)

    class Show(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "looks_show", shadow=shadow, pos=pos)

    class GoToFrontBack(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "looks_gotofrontback", shadow=shadow, pos=pos)

        def set_front_back(self, value: str = "front", value_id: str = None):
            return self.add_field(Field("FRONT_BACK", value, value_id))

    class GoForwardBackwardLayers(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "looks_goforwardbackwardlayers", shadow=shadow, pos=pos)

        def set_num(self, value="1", input_type: str | int = "positive integer", shadow_status: int = 1, *,
                    input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("NUM", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

        def set_fowrward_backward(self, value: str = "forward", value_id: str = None):
            return self.add_field(Field("FORWARD_BACKWARD", value, value_id))

    class CostumeNumberName(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "looks_costumenumbername", shadow=shadow, pos=pos)

        def set_number_name(self, value: str = "string", value_id: str = None):
            return self.add_field(Field("NUMBER_NAME", value, value_id))

    class BackdropNumberName(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "looks_backdropnumbername", shadow=shadow, pos=pos)

        def set_number_name(self, value: str = "number", value_id: str = None):
            return self.add_field(Field("NUMBER_NAME", value, value_id))

    class Size(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "looks_size", shadow=shadow, pos=pos)

    class HideAllSprites(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "looks_hideallsprites", shadow=shadow, pos=pos)

    class SetStretchTo(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "looks_setstretchto", shadow=shadow, pos=pos)

        def set_stretch(self, value="100", input_type: str | int = "number", shadow_status: int = 1, *,
                        input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("STRETCH", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class ChangeStretchBy(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "looks_changestretchby", shadow=shadow, pos=pos)

        def set_change(self, value="10", input_type: str | int = "number", shadow_status: int = 1, *,
                       input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("CHANGE", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))


class Sounds:
    class Play(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "sound_play", shadow=shadow, pos=pos)

        def set_sound_menu(self, value, input_type: str | int = "block", shadow_status: int = 1, *,
                           input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("SOUND_MENU", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class SoundsMenu(Block):
        def __init__(self, *, shadow: bool = True, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "sound_sounds_menu", shadow=shadow, pos=pos)

        def set_sound_menu(self, value: str = "pop", value_id: str = None):
            return self.add_field(Field("SOUND_MENU", value, value_id))

    class PlayUntilDone(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "sound_playuntildone", shadow=shadow, pos=pos)

        def set_sound_menu(self, value, input_type: str | int = "block", shadow_status: int = 1, *,
                           input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("SOUND_MENU", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class StopAllSounds(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "sound_stopallsounds", shadow=shadow, pos=pos)

    class ChangeEffectBy(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "sound_changeeffectby", shadow=shadow, pos=pos)

        def set_value(self, value="10", input_type: str | int = "number", shadow_status: int = 1, *,
                      input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("VALUE", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

        def set_effect(self, value: str = "PITCH", value_id: str = None):
            return self.add_field(Field("EFFECT", value, value_id))

    class SetEffectTo(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "sound_seteffectto", shadow=shadow, pos=pos)

        def set_value(self, value="100", input_type: str | int = "number", shadow_status: int = 1, *,
                      input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("VALUE", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

        def set_effect(self, value: str = "PITCH", value_id: str = None):
            return self.add_field(Field("EFFECT", value, value_id))

    class ClearEffects(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "sound_cleareffects", shadow=shadow, pos=pos)

    class ChangeVolumeBy(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "sound_changevolumeby", shadow=shadow, pos=pos)

        def set_volume(self, value="-10", input_type: str | int = "number", shadow_status: int = 1, *,
                       input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("VOLUME", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class SetVolumeTo(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "sound_setvolumeto", shadow=shadow, pos=pos)

        def set_volume(self, value="100", input_type: str | int = "number", shadow_status: int = 1, *,
                       input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("VOLUME", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class Volume(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "sound_volume", shadow=shadow, pos=pos)


class Events:
    class WhenFlagClicked(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "event_whenflagclicked", shadow=shadow, pos=pos)

    class WhenKeyPressed(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "event_whenkeypressed", shadow=shadow, pos=pos)

        def set_key_option(self, value: str = "space", value_id: str = None):
            return self.add_field(Field("KEY_OPTION", value, value_id))

    class WhenThisSpriteClicked(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "event_whenthisspriteclicked", shadow=shadow, pos=pos)

    class WhenStageClicked(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "event_whenstageclicked", shadow=shadow, pos=pos)

    class WhenBackdropSwitchesTo(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "event_whenbackdropswitchesto", shadow=shadow, pos=pos)

        def set_backdrop(self, value: str = "backdrop1", value_id: str = None):
            return self.add_field(Field("BACKDROP", value, value_id))

    class WhenGreaterThan(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "event_whengreaterthan", shadow=shadow, pos=pos)

        def set_value(self, value="10", input_type: str | int = "number", shadow_status: int = 1, *,
                      input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("VALUE", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

        def set_when_greater_than_menu(self, value: str = "LOUDNESS", value_id: str = None):
            return self.add_field(Field("WHENGREATERTHANMENU", value, value_id))

    class WhenBroadcastReceived(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "event_whenbroadcastreceived", shadow=shadow, pos=pos)

        def set_broadcast_option(self, value="message1", value_id: str = "I didn't get an id..."):
            return self.add_field(Field("BROADCAST_OPTION", value, value_id))

    class Broadcast(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "event_broadcast", shadow=shadow, pos=pos)

        def set_broadcast_input(self, value="message1", input_type: str | int = "broadcast", shadow_status: int = 1, *,
                                input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("BROADCAST_INPUT", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class BroadcastAndWait(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "event_broadcastandwait", shadow=shadow, pos=pos)

        def set_broadcast_input(self, value="message1", input_type: str | int = "broadcast", shadow_status: int = 1, *,
                                input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("BROADCAST_INPUT", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class WhenTouchingObject(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "event_whentouchingobject", shadow=shadow, pos=pos)

        def set_touching_object_menu(self, value, input_type: str | int = "block", shadow_status: int = 1, *,
                                     input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("TOUCHINGOBJECTMENU", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class TouchingObjectMenu(Block):
        def __init__(self, *, shadow: bool = True, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "event_touchingobjectmenu", shadow=shadow, pos=pos)

        def set_touching_object_menu(self, value: str = "_mouse_", value_id: str = None):
            return self.add_field(Field("TOUCHINGOBJECTMENU", value, value_id))


class Control:
    class Wait(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "control_wait", shadow=shadow, pos=pos)

        def set_duration(self, value="1", input_type: str | int = "number", shadow_status: int = 1, *,
                         input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("DURATION", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class Forever(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "control_forever", shadow=shadow, pos=pos, can_next=False)

        def set_substack(self, value, input_type: str | int = "block", shadow_status: int = 2, *,
                         input_id: str = None):
            inp = Input("SUBSTACK", value, input_type, shadow_status, input_id=input_id)
            return self.add_input(inp)

    class If(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "control_if", shadow=shadow, pos=pos)

        def set_substack(self, value, input_type: str | int = "block", shadow_status: int = 2, *,
                         input_id: str = None):
            inp = Input("SUBSTACK", value, input_type, shadow_status, input_id=input_id)
            return self.add_input(inp)

        def set_condition(self, value, input_type: str | int = "block", shadow_status: int = 2, *,
                          input_id: str = None):
            inp = Input("CONDITION", value, input_type, shadow_status, input_id=input_id)
            return self.add_input(inp)

    class IfElse(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "control_if_else", shadow=shadow, pos=pos)

        def set_substack1(self, value, input_type: str | int = "block", shadow_status: int = 2, *,
                          input_id: str = None):
            inp = Input("SUBSTACK", value, input_type, shadow_status, input_id=input_id)
            return self.add_input(inp)

        def set_substack2(self, value, input_type: str | int = "block", shadow_status: int = 2, *,
                          input_id: str = None):
            inp = Input("SUBSTACK2", value, input_type, shadow_status, input_id=input_id)
            return self.add_input(inp)

        def set_condition(self, value, input_type: str | int = "block", shadow_status: int = 2, *,
                          input_id: str = None):
            inp = Input("CONDITION", value, input_type, shadow_status, input_id=input_id)
            return self.add_input(inp)

    class WaitUntil(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "control_wait_until", shadow=shadow, pos=pos)

        def set_condition(self, value, input_type: str | int = "block", shadow_status: int = 1, *,
                          input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("CONDITION", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class RepeatUntil(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "control_repeat_until", shadow=shadow, pos=pos)

        def set_substack(self, value, input_type: str | int = "block", shadow_status: int = 2, *,
                         input_id: str = None):
            inp = Input("SUBSTACK", value, input_type, shadow_status, input_id=input_id)
            return self.add_input(inp)

        def set_condition(self, value, input_type: str | int = "block", shadow_status: int = 2, *,
                          input_id: str = None):
            inp = Input("CONDITION", value, input_type, shadow_status, input_id=input_id)
            return self.add_input(inp)

    class While(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "control_while", shadow=shadow, pos=pos)

        def set_substack(self, value, input_type: str | int = "block", shadow_status: int = 2, *,
                         input_id: str = None):
            inp = Input("SUBSTACK", value, input_type, shadow_status, input_id=input_id)
            return self.add_input(inp)

        def set_condition(self, value, input_type: str | int = "block", shadow_status: int = 2, *,
                          input_id: str = None):
            inp = Input("CONDITION", value, input_type, shadow_status, input_id=input_id)
            return self.add_input(inp)

    class Stop(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "control_stop", shadow=shadow, pos=pos, mutation=Mutation())

        def set_stop_option(self, value: str = "all", value_id: str = None):
            return self.add_field(Field("STOP_OPTION", value, value_id))

        def set_hasnext(self, has_next: bool = True):
            self.mutation.has_next = has_next
            return self

    class StartAsClone(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "control_start_as_clone", shadow=shadow, pos=pos)

    class CreateCloneOf(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "control_create_clone_of", shadow=shadow, pos=pos)

        def set_clone_option(self, value, input_type: str | int = "block", shadow_status: int = 1, *,
                             input_id: str = None, obscurer: str | Block = None):
            return self.add_input(
                Input("CLONE_OPTION", value, input_type, shadow_status, input_id=input_id, obscurer=obscurer))

    class CreateCloneOfMenu(Block):
        def __init__(self, *, shadow: bool = True, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "control_create_clone_of_menu", shadow=shadow, pos=pos)

        def set_clone_option(self, value: str = "_myself_", value_id: str = None):
            return self.add_field(Field("CLONE_OPTION", value, value_id))


class Sensing:
    class TouchingObjectMenu(Block):
        def __init__(self, *, shadow: bool = True, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "sensing_touchingobjectmenu", shadow=shadow, pos=pos)

        def set_touching_object_menu(self, value: str = "_mouse_", value_id: str = None):
            return self.add_field(Field("TOUCHINGOBJECTMENU", value, value_id))

    class Loud(Block):
        def __init__(self, *, shadow: bool = False, pos: tuple[int | float, int | float] = (0, 0)):
            super().__init__(None, "sensing_loud", shadow=shadow, pos=pos)


# class Data:
#     class Variable(Block):
#         def __init__(self, *, shadow: bool = True, pos: tuple[int | float, int | float] = (0, 0)):
#             super().__init__(None, "data_variable", shadow=shadow, pos=pos)
#

def link_chain(*_chain: [Block], target: Target = None) -> [Block]:
    """
    Attaches a chain together so that the parent/next attributes are linked to the relevant blocks.

    Useful for chains that are a substack of a C-Mouth, to input the chain's first item while simultaneously linking the
    chain together without setting variables
    :param _chain: Blockchain (List/tuple of blocks)
    :param target: Target to attach to the first block
    :return: The chain you gave in
    """
    if _chain[0].target is None and target is not None:
        target.add_block(_chain[0])

    _chain[0].attach_chain(
        _chain[1:]
    )

    return _chain

