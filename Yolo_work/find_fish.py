from ultralytics import YOLO
from ultralytics.engine.results import Results

class FindFish:
    '''Image detection for fish'''
    def __init__(self):
        pass

    def __best_bbox(self, boxes : list[list[tuple, float]]) -> tuple[tuple, float]:
        '''Finds the box with the highest confidence'''
        best_box : tuple[tuple, float] = boxes[0]
        for box in boxes:
            if box[1] > best_box[1]:
                best_box = box
        return best_box

    def locate_fish_bbox(self, image_path : str) -> tuple[tuple, float]:
        '''Find the location of a fish in an image if one is present'''
        model : YOLO = YOLO("runs/detect/train2/weights/best.pt")
        results : list[Results] = model(source=image_path)
        bboxes : list[tuple[tuple, float]]= []
        for result in results:
            if result.boxes is None:
                continue

            for box in result.boxes:
                x0, y0, x1, y1 = box.xyxy[0].tolist()
                confidence : float = float(box.conf[0])
                if confidence > 0.1:
                    bboxes.append(((x0, y0, x1, y1), confidence))
        best_bbox : tuple[tuple, float] = self.__best_bbox(bboxes)
        return best_bbox