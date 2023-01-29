from pathlib import Path

from peekingduck.pipeline.nodes.dabble import fps , tracking ,statistics,bbox_count
from peekingduck.pipeline.nodes.draw import bbox, legend
from peekingduck.pipeline.nodes.input import visual
from peekingduck.pipeline.nodes.model import yolo , efficientdet
from peekingduck.pipeline.nodes.output import media_writer, screen,csv_writer
from peekingduck.runner import Runner
from src.custom_nodes.dabble import debug

def main():
    debug_node = debug.Node(pkd_base_dir=Path.cwd() / "src" / "custom_nodes")
    visual_node = visual.Node(source=str(Path.cwd() / "Video Of People Walking.mp4"))
    effdetect_node = efficientdet.Node(detect=["person"])
    tracking_node = tracking.Node(type = "iou")
    statistics_node = statistics.Node(maximum = "ids")
    bbox_count_node = bbox_count.Node()
    csv_writer_node = csv_writer.Node(file_path=str(Path.cwd() / "output" / "new.csv"),stats_to_track= ['cum_max','count'])
    runner = Runner(
        nodes=[visual_node,
            effdetect_node,
            debug_node,
            tracking_node,
            statistics_node,
            bbox_count_node,
            csv_writer_node]
        
    )
    runner.run()

main()