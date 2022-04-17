import riotwatcher as rw


def get_summoner_info(
    configs: dict
):
    watcher = rw.LolWatcher(
        api_key=configs["api-key"]
    )

    summoner_id = watcher.summoner.by_name(
        region=configs["summoner"]["region"],
        summoner_name=configs["summoner"]["name"]
    )["id"]

    summoner_info = watcher.league.by_summoner(
        region=configs["summoner"]["region"],
        encrypted_summoner_id=summoner_id
    )

    return summoner_info[0]


if __name__ == "__main__":
    import tools as t
    
    configs = t.get_yaml_configs()

    get_summoner_info(
        configs=configs,
    )
