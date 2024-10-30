from .sbuild import *


proj = Project.from_sb3("Weekend.sb3")

sprite = proj.targets[4]
my_var = sprite.add_variable("test")

chain = sprite.get_blocks_by_opcode("event_whenflagclicked")[0].stack_chain()

block = chain[-1]

script = (
    # Motion blocks
    Motion.MoveSteps()
    .set_steps("10"),

    Motion.TurnRight()
    .set_degrees("90"),

    Motion.TurnLeft()
    .set_degrees("-45", "angle"),

    Motion.GoTo()
    .set_to(sprite.add_block(Motion.GoToMenu()
                             .set_to("_random_"))),

    Motion.GoToXY()
    .set_x("100")
    .set_y("100"),

    Motion.GlideTo()
    .set_secs(5)
    .set_to(sprite.add_block(Motion.GlideToMenu()
                             .set_to("_random_"))),

    Motion.GlideSecsToXY()
    .set_x("100")
    .set_y("100")
    .set_secs("3"),

    Motion.PointInDirection()
    .set_direction("90"),

    Motion.PointTowards()
    .set_towards(sprite.add_block(Motion.PointTowardsMenu()
                                  .set_towards("_random_"))),

    Motion.ChangeXBy()
    .set_dx("10"),

    Motion.ChangeYBy()
    .set_dy("10"),

    Motion.SetX()
    .set_x("100"),

    Motion.SetY()
    .set_y("100"),

    Motion.IfOnEdgeBounce(),

    Motion.SetRotationStyle()
    .set_style("left-right"),

    Looks.Say()
    .set_message(sprite.add_block(Motion.XPosition())),

    Looks.Say()
    .set_message(sprite.add_block(Motion.YPosition())),

    Looks.Say()
    .set_message(sprite.add_block(Motion.Direction())),

    Motion.ScrollRight()
    .set_distance("10"),

    Motion.ScrollUp()
    .set_distance("10"),

    Motion.AlignScene()
    .set_alignment(),

    Looks.Say()
    .set_message(sprite.add_block(Motion.XScroll())),

    Looks.Say()
    .set_message(sprite.add_block(Motion.YScroll())),

    # Looks blocks
    Looks.SayForSecs()
    .set_message("Hello!")
    .set_secs("2"),

    Looks.Say()
    .set_message("Hello!"),

    Looks.ThinkForSecs()
    .set_message("Hmm...")
    .set_secs("2"),

    Looks.Think()
    .set_message("Hmm..."),

    Looks.SwitchCostumeTo()
    .set_costume(sprite.add_block(Looks.Costume()
                                  .set_costume("previous costume"))),

    Looks.NextCostume(),

    Looks.SwitchBackdropTo()
    .set_backdrop(sprite.add_block(Looks.Backdrops()
                                   .set_backdrop("previous backdrop"))),

    Looks.SwitchBackdropToAndWait()
    .set_backdrop(sprite.add_block(Looks.Backdrops()
                                   .set_backdrop("previous backdrop"))),
    Looks.ChangeSizeBy()
    .set_change("10"),

    Looks.SetSizeTo()
    .set_size("100"),

    Looks.ChangeEffectBy()
    .set_change("25")
    .set_effect("COLOR"),

    Looks.SetEffectTo()
    .set_value("100")
    .set_effect("COLOR"),

    Looks.ClearGraphicEffects(),

    Looks.Show(),

    Looks.Hide(),

    Looks.GoToFrontBack()
    .set_front_back("back"),

    Looks.GoForwardBackwardLayers()
    .set_num("3")
    .set_fowrward_backward("forward"),

    Looks.Say()
    .set_message(sprite.add_block(Looks.CostumeNumberName()
                                  .set_number_name("name"))),

    Looks.Say()
    .set_message(sprite.add_block(Looks.BackdropNumberName()
                                  .set_number_name("name"))),

    Looks.Say()
    .set_message(sprite.add_block(Looks.Size())),

    Looks.HideAllSprites(),

    Looks.SetStretchTo()
    .set_stretch("75"),

    Looks.ChangeStretchBy()
    .set_change("50"),

    # Sounds
    Sounds.Play()
    .set_sound_menu(sprite.add_block(Sounds.SoundsMenu()
                                     .set_sound_menu("poopie"))),

    Sounds.PlayUntilDone()
    .set_sound_menu(sprite.add_block(Sounds.SoundsMenu()
                                     .set_sound_menu("poopie"))),

    Sounds.StopAllSounds(),

    Sounds.ChangeEffectBy()
    .set_effect("PAN")
    .set_value("30"),

    Sounds.SetEffectTo()
    .set_effect("PITCH")
    .set_value("16"),

    Sounds.ClearEffects(),

    Sounds.ChangeVolumeBy()
    .set_volume("25"),

    Sounds.SetVolumeTo()
    .set_volume("100"),

    # Events
    Events.Broadcast()
    .set_broadcast_input(
        sprite.add_broadcast("hello")
    ),

    Events.BroadcastAndWait()
    .set_broadcast_input(
        sprite.get_broadcast_by_name("hello")
    ),

    Control.IfElse()
    .set_condition(
        sprite.add_block(
            Sensing.Loud()
        )
    )
    .set_substack1(
        link_chain(
            Looks.Say()
            .set_message("Wow this works"),

            Motion.MoveSteps()
            .set_steps("#FF0000", "color", shadow_status=2),
            target=sprite)[0]
    )
    .set_substack2(
        link_chain(
            Looks.Think()
            .set_message("Wow, you're being quiet for once"),

            Control.Wait()
            .set_duration("3"),

            Control.If()
            .set_condition(
                sprite.add_block(Sensing.Loud())
            )
            .set_substack(
                link_chain(
                    Looks.SayForSecs()
                    .set_message("I was thinking about how quiet you were")
                    .set_secs("2"),

                    Looks.ThinkForSecs()
                    .set_message("But now you are so loud I can't even think")
                    .set_secs("agh"),
                    target=sprite)[0],
            ),
            target=sprite)[0]
    ),

    Control.Stop()
    .set_stop_option("buhing")
    .set_hasnext(True),

    Control.CreateCloneOf()
    .set_clone_option(
        sprite.add_block(Control.CreateCloneOfMenu()
                         .set_clone_option("the scratchattach github repo"))
    )
)
block.attach_chain(script)

# Events blocks
sprite.add_block(Events.WhenFlagClicked())
sprite.add_block(Events.WhenKeyPressed()
                 .set_key_option(","))

sprite.add_block(Events.WhenTouchingObject()
.set_touching_object_menu(
    sprite.add_block(Events.TouchingObjectMenu()
                     .set_touching_object_menu("_mouse_"))
))

sprite.add_block(Block.from_input(Input(None, my_var)))

# Control.Forever()
# .set_substack(
#     link_chain(
#         sprite.add_block(Motion.MoveSteps()
#                          .set_steps("10")),
#         Motion.GoToXY()
#         .set_x("0")
#         .set_y("0")
#     )[0]
# )
proj.save_json()
proj.export("test proj")
