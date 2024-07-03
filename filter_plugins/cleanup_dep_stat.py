class FilterModule(object):

    def filters(self):
        return {
            'cleanup_dep_stat': self.cleanup_dep_stat,
        }

    def cleanup_dep_stat(self, value, deployment):
        for item in value['items']:
            if item["severity"] == critical:
                return item["actual"]
        return None  # Eğer hiçbir eşleşme bulunmazsa None döndürmek iyi bir uygulama olabilir
