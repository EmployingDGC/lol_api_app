import riotwatcher as rw


def get_summoner_info(
    configs: dict
):
    api_key = configs["api-key"]
    summoner = configs["summoner"]

    queue_type = summoner["queue_type"].upper()

    watcher = rw.LolWatcher(
        api_key=api_key
    )

    summoner_id = watcher.summoner.by_name(
        region=summoner["region"],
        summoner_name=summoner["name"]
    )["id"]

    summoner_info = watcher.league.by_summoner(
        region=summoner["region"],
        encrypted_summoner_id=summoner_id
    )

    for si in summoner_info:
        if queue_type == si["queueType"].upper():
            return si

    return None


if __name__ == "__main__":
    import tools as t

    configs = t.get_yaml_configs()

    summoner_info = get_summoner_info(
        configs=configs,
    )

    print(summoner_info)
