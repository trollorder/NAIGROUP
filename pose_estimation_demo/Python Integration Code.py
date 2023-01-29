from pathlib import Path

from peekingduck.pipeline.nodes.dabble import fps
from peekingduck.pipeline.nodes.draw import bbox, legend
from peekingduck.pipeline.nodes.input import visual
from peekingduck.pipeline.nodes.model import yolo
from peekingduck.pipeline.nodes.output import media_writer, screen,csv_writer
from peekingduck.runner import Runner
from src.custom_nodes.dabble import debug

def main():
    debug_node = debug.Node(pkd_base_dir=Path.cwd() / "src" / "custom_nodes")

    visual_node = visual.Node(source=str(Path.cwd() / "Video Of People Walking.mp4"))
    yolo_node = yolo.Node(detect=["person"])
    bbox_node = bbox.Node(show_labels=True)

    fps_node = fps.Node()
    legend_node = legend.Node(show=["fps"])
    screen_node = screen.Node()

    csv_writer_node = csv_writer.Node(file_path=str(Path.cwd() / "output" / "new.csv"))

    runner = Runner(
        nodes=[
            visual_node,
            yolo_node,
            debug_node,
            bbox_node,
            fps_node,
            legend_node,
            screen_node,
            csv_writer_node,
        ]
    )
    print(runner)
    runner.run()

main()