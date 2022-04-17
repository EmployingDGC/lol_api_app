import get_summoner_info as gsi


def write_file(
    path: str,
    text: str
):
    with open(
        file=path,
        mode="w"
    ) as f:
        f.write(text)


def main(
    configs: dict
):
    summoner_info = gsi.get_summoner_info(
        configs=configs
    )

    pdl = summoner_info["leaguePoints"]
    tier = summoner_info["tier"]

    text = f"{str(tier).title()} {pdl} pdl"

    write_file(
        path="./pdl.txt",
        text=text
    )


if __name__ == "__main__":
    import tools as t

    configs = t.get_yaml_configs()

    main(
        configs=configs
    )
