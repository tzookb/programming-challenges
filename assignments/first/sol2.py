# test id - 23280666631255
import collections
import functools

class Scene:
    def __init__(self, start, end):
        self.frames = {}
        self.start = start
        self.end = end

    def addFrame(self, frame):
        self.frames[frame] = True

    def addFrames(self, frames):
        for frame in frames:
            self.addFrame(frame)

    def getFrames(self):
        framesArr = []
        for frame in self.frames:
            framesArr.append(frame)
        return framesArr

    def isFrameExists(self, frame):
        # print("frame")
        # print(frame)
        # print(self.frames)
        return frame in self.frames

    def setEnd(self, end):
        self.end = end

    def setStart(self, start):
        self.start = start
    

def printScenes(scenes):
    for scene in scenes:
        print("scene:")
        print(scene.start, scene.end)
        print(scene.frames)

def getScenesSizes(scenes):
    sizes = []
    for scene in scenes:
        sizes.append(scene.end - scene.start + 1)
    return sizes

def mergeScenes(scenes, fromIdx):
    endScenes = scenes[:fromIdx]
    
    toMerge = scenes[fromIdx:]

    mergedScene = Scene(toMerge[0].start, toMerge[-1].end+1)
    for scene in toMerge:
        mergedScene.addFrames(
            scene.getFrames()
        )
    endScenes.append(mergedScene)
    return endScenes

def lengthEachScene(inputList):
    scenes = []

    for idx, frame in enumerate(inputList):
        merged = False
        i = len(scenes) - 1
        
        while i >= 0:
            # printScenes(scenes)
            scene = scenes[i]
            if scene.isFrameExists(frame):
                scenes = mergeScenes(scenes, i)
                merged = True
                break
            i -= 1

        if not merged:
            newScene = Scene(idx, idx)
            newScene.addFrame(frame)
            scenes.append(newScene)
    
    # printScenes(scenes)

    return getScenesSizes(scenes)

        
        

res = lengthEachScene([
    "a", "b", "a", "c", "a", "d"
])

print(res)