from pathlib import Path

from peekingduck.pipeline.nodes.dabble import fps , tracking ,statistics,bbox_count,zone_count,bbox_to_btm_midpoint
from peekingduck.pipeline.nodes.draw import bbox, legend,zones
from peekingduck.pipeline.nodes.input import visual
from peekingduck.pipeline.nodes.model import yolo , efficientdet
from peekingduck.pipeline.nodes.output import media_writer, screen,csv_writer
from peekingduck.runner import Runner
from src.custom_nodes.dabble import debug
from src.custom_nodes.output import traincountsqlite

def main():
    debug_node = debug.Node(pkd_base_dir=Path.cwd() / "src" / "custom_nodes")
    visual_node = visual.Node(source=str(Path.cwd() / "Video Testing/Queue 2.mp4"))
    effdetect_node = efficientdet.Node(detect=["person"])
    statistics_node = statistics.Node(maximum='obj_attrs["ids"]')
    tracking_node = tracking.Node(type = "iou")
    bbox_count_node = bbox_count.Node()
    csv_writer_node = csv_writer.Node(file_path=str(Path.cwd() / "output" / "new.csv"),stats_to_track= ['obj_attrs','cum_max','count'])
    traincountsqlite_node = traincountsqlite.Node()
    screen_node=screen.Node()
    zonecount_node = zone_count.Node(zones =[[[0, 0], [0.6, 0], [0.6, 1], [0, 1]],[[0.6, 0], [1, 0], [1, 1], [0.6, 1]]])
    bboxtobtmmidpt_node=bbox_to_btm_midpoint.Node()
    zone_node = zones.Node()
    bbox_node=bbox.Node()
    
    runner = Runner(
        nodes=[visual_node,
            effdetect_node,
            tracking_node,
            bboxtobtmmidpt_node,
            bbox_count_node,
            zonecount_node,
            screen_node,
            bbox_node,
            zone_node,
            traincountsqlite_node]
        
    )
    runner.run()
    

main()