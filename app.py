import gradio as gr


def cadmate(part, question):
    if not part:
        return "Please select a mechanical part."

    question = question or ""

    response = f"""CADMate AI Analysis

Part: {part}

"""

    if part == "Gear":
        response += """Recommended starting design:
• Module: 2 mm
• Number of teeth: 20
• Pitch diameter: 40 mm
• Face width: 15 mm
• Bore diameter: 20 mm

Material:
Medium Carbon Steel

Manufacturing:
• Gear hobbing
• CNC machining
• Heat treatment if required

AutoCAD workflow:
1. Draw the pitch circle.
2. Create the gear tooth profile.
3. Create a polar array for the teeth.
4. Create the centre bore.
5. Add dimensions and centre lines.
6. Prepare the final 2D drawing.
"""

    elif part == "Flange Coupling":
        response += """Recommended starting design:
• Shaft diameter: 25 mm
• Flange diameter: 100 mm
• Flange thickness: 12 mm
• Number of bolts: 4

Material:
Mild Steel

Manufacturing:
• Turning
• Drilling
• CNC machining

AutoCAD workflow:
1. Draw the flange.
2. Create the shaft bore.
3. Create the bolt circle.
4. Position the bolt holes equally.
5. Add dimensions and centre lines.
"""

    elif part == "Shaft":
        response += """Basic design guidance:
• Define shaft diameter and length.
• Consider the transmitted torque.
• Select a suitable steel grade.
• Add keyways or shoulders where required.

Manufacturing:
• CNC turning
• Drilling
• Keyway machining

AutoCAD:
Create the shaft profile, add centre lines, dimensions and tolerances.
"""

    elif part == "Bearing":
        response += """Basic design guidance:
• Select bearing type according to load and speed.
• Check shaft and housing dimensions.
• Consider radial and axial loads.

Manufacturing:
Precision machining and grinding are commonly used.

AutoCAD:
Create the bearing section/profile and add important dimensions.
"""

    elif part == "Pulley":
        response += """Basic design guidance:
• Define pulley diameter and width.
• Select the required belt type.
• Check shaft and bore dimensions.

Material:
Cast iron or suitable aluminium/steel depending on application.

Manufacturing:
• Casting
• CNC machining
• Turning

AutoCAD:
Create the pulley profile, groove geometry, bore and dimensions.
"""

    else:
        response += "Basic CAD analysis is available for this component."

    response += f"""

Your question:
{question}

Design note:
These are preliminary educational recommendations. Final engineering dimensions should be verified using appropriate design calculations and standards.
"""

    return response


with gr.Blocks(title="CADMate AI") as app:

    gr.Markdown(
        """
        # 🔧 CADMate AI
        ### AI-Powered Mechanical CAD Design Assistant

        **Design → Material → Manufacturing → CAD**
        """
    )

    part = gr.Dropdown(
        choices=[
            "Gear",
            "Flange Coupling",
            "Shaft",
            "Bearing",
            "Pulley"
        ],
        label="Select Mechanical Part"
    )

    question = gr.Textbox(
        label="Ask CADMate AI",
        placeholder="Example: What material should I use?",
        lines=3
    )

    button = gr.Button("Analyze Design")

    output = gr.Textbox(
        label="CADMate AI Result",
        lines=20
    )

    button.click(
        fn=cadmate,
        inputs=[part, question],
        outputs=output
    )


if __name__ == "__main__":
    app.launch()
