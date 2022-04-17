import get_summoner_info as gsi


def main(
    configs: dict
):
    summoner_info = gsi.get_summoner_info(
        configs=configs
    )

    pdl = summoner_info["leaguePoints"]

    print(pdl)


if __name__ == "__main__":
    import tools as t
    
    configs = t.get_yaml_configs()

    main(
        configs=configs
    )
