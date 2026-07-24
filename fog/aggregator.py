class DataAggregator:
   
    @staticmethod
    def aggregate(readings):

        values = [reading["value"] for reading in readings]

        return {
            "reading_count": len(values),
            "minimum": round(min(values), 2),
            "maximum": round(max(values), 2),
            "average": round(sum(values) / len(values), 2)
        }