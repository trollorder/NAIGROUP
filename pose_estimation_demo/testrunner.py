from pathlib import Path

from peekingduck.pipeline.nodes.dabble import fps
from peekingduck.pipeline.nodes.draw import bbox, legend
from peekingduck.pipeline.nodes.input import visual
from peekingduck.pipeline.nodes.model import yolo
from peekingduck.pipeline.nodes.output import media_writer, screen
from peekingduck.runner import Runner
from src.custom_nodes.dabble import debug


def main():
    debug_node = debug.Node(pkd_base_dir=Path.cwd() / "src" / "custom_nodes")

    visual_node = visual.Node(source=str(Path.cwd() / "gatos.mp4"))
    yolo_node = yolo.Node(detect=["cup", "cat", "laptop", "keyboard", "mouse"])
    bbox_node = bbox.Node(show_labels=True)

    fps_node = fps.Node()
    legend_node = legend.Node(show=["fps"])
    screen_node = screen.Node()

    media_writer_node = media_writer.Node(output_dir=str(Path.cwd() / "results"))

    runner = Runner(
        nodes=[
            visual_node,
            yolo_node,
            debug_node,
            bbox_node,
            fps_node,
            legend_node,
            screen_node,
            media_writer_node,
        ]
    )
    runner.run()


if __name__ == "__main__":
    main()