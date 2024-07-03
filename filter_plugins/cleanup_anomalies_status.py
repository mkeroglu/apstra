class FilterModule(object):

    def filters(self):
        return {
            'cleanup_dep_stat': self.cleanup_dep_stat,
        }

    def cleanup_dep_stat(self, value, bp_name):
        for item in value['items']:
            if item["anomaly_type"] == deployment:
                return (item["id"])
