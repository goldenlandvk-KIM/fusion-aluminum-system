import adsk.core
import adsk.fusion
import traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface

        product = app.activeProduct
        design = adsk.fusion.Design.cast(product)
        if not design:
            ui.messageBox("当前不是 Design 工作区")
            return

        rootComp = design.rootComponent

        def create_post(x, y, z, name):
            transform = adsk.core.Matrix3D.create()
            transform.translation = adsk.core.Vector3D.create(x, y, z)
            occ = rootComp.occurrences.addNewComponent(transform)
            comp = occ.component
            comp.name = name

            sketch = comp.sketches.add(comp.xYConstructionPlane)
            lines = sketch.sketchCurves.sketchLines
            lines.addTwoPointRectangle(
                adsk.core.Point3D.create(0, 0, 0),
                adsk.core.Point3D.create(4, 4, 0)
            )

            profile = sketch.profiles.item(0)
            extrudes = comp.features.extrudeFeatures
            extrudeInput = extrudes.createInput(
                profile,
                adsk.fusion.FeatureOperations.NewBodyFeatureOperation
            )
            distance = adsk.core.ValueInput.createByReal(50)
            extrudeInput.setDistanceExtent(False, distance)
            extrudes.add(extrudeInput)

        create_post(0, 0, 0, "Post_1")
        create_post(20, 0, 0, "Post_2")
        create_post(0, 10, 0, "Post_3")
        create_post(20, 10, 0, "Post_4")

        ui.messageBox("成功生成4根立柱")

    except:
        if ui:
            ui.messageBox("Failed:\n{}".format(traceback.format_exc()))import adsk.core
import adsk.fusion
import traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface

        product = app.activeProduct
        design = adsk.fusion.Design.cast(product)
        if not design:
            ui.messageBox("当前不是 Design 工作区")
            return

        rootComp = design.rootComponent

        def create_post(x, y, z, name):
            transform = adsk.core.Matrix3D.create()
            transform.translation = adsk.core.Vector3D.create(x, y, z)
            occ = rootComp.occurrences.addNewComponent(transform)
            comp = occ.component
            comp.name = name

            sketch = comp.sketches.add(comp.xYConstructionPlane)
            lines = sketch.sketchCurves.sketchLines
            lines.addTwoPointRectangle(
                adsk.core.Point3D.create(0, 0, 0),
                adsk.core.Point3D.create(4, 4, 0)
            )

            profile = sketch.profiles.item(0)
            extrudes = comp.features.extrudeFeatures
            extrudeInput = extrudes.createInput(
                profile,
                adsk.fusion.FeatureOperations.NewBodyFeatureOperation
            )
            distance = adsk.core.ValueInput.createByReal(50)
            extrudeInput.setDistanceExtent(False, distance)
            extrudes.add(extrudeInput)

        create_post(0, 0, 0, "Post_1")
        create_post(20, 0, 0, "Post_2")
        create_post(0, 10, 0, "Post_3")
        create_post(20, 10, 0, "Post_4")

        ui.messageBox("成功生成4根立柱")

    except:
        if ui:
            ui.messageBox("Failed:\n{}".format(traceback.format_exc()))
