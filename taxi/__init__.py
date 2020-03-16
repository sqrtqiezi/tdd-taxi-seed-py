""" Taxi """
import re


def process_file(path):
    result = []
    with open(path, "r") as file:
        line = file.readline()
        while line:
            m = re.match(r"(?P<distance>\d+)公里,等待(?P<minutes>\d+)", line)
            distance, minutes = int(m.group("distance")), int(m.group("minutes"))
            fee = 6
            if distance > 2:
                if distance <= 8:
                    fee = fee + (distance - 2) * 0.8
                else:
                    fee = fee + 6 * 0.8 + (distance - 8) * 1.2
            if minutes > 0:
                fee = fee + minutes * 0.25
            result.append("收费%s元" % round(fee))
            line = file.readline()
    return "\n".join(result)
