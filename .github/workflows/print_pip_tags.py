from pip._internal.models.target_python import TargetPython


target = TargetPython()


for t in target.get_tags():
    print(t)
