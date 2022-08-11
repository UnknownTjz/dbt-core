import click
from dbt.cli.params.types import YAML

log_path = click.option(
    "--log-path",
    help="Configure the 'log-path'. Only applies this setting for the current run. Overrides the 'DBT_LOG_PATH' if it is set.",
    type=click.Path(),
)

target_path = click.option(
    "--target-path",
    help="Configure the 'target-path'. Only applies this setting for the current run. Overrides the 'DBT_TARGET_PATH' if it is set.",
    type=click.Path(),
)

threads = click.option(
    "--threads",
    help="Specify number of threads to use while executing models. Overrides settings in profiles.yml.",
    default=1,
    type=click.INT,
)

models = click.option("-m", "-s", help="Specify the nodes to include.", multiple=True)

exclude = click.option("--exclude", help="Specify the nodes to exclude.")

selector = click.option("--selector", help="The selector name to use, as defined in selectors.yml")

state = click.option(
    "--state",
    help="If set, use the given directory as the source for json files to compare with this project.",
)

defer = click.option(
    "--defer/--no-defer",
    help="If set, defer to the state variable for resolving unselected nodes.",
    default=True,
)

full_refresh = click.option(
    "--full-refresh",
    help="If specified, dbt will drop incremental models and fully-recalculate the incremental table from the model definition.",
    is_flag=True,
)

parse_only = click.option(
    "--parse-only",
    help="TODO:  No help text currently available",
    is_flag=True,
)

resource_type = click.option(
    "--resource-type",
    help="TODO: No current help text",
    type=click.Choice(
        [
            "metric",
            "source",
            "analysis",
            "model",
            "test",
            "exposure",
            "snapshot",
            "seed",
            "default",
            "all",
        ],
        case_sensitive=False,
    ),
    default="default",
)

indirect_selection = click.option(
    "--indirect_selection",
    help="Select all tests that are adjacent to selected resources, even if they those resources have been explicitly selected.",
    type=click.Choice(["eager", "cautious"], case_sensitive=False),
    default="eager",
)

args = click.option(
    "--args",
    help="Supply arguments to the macro. This dictionary will be mapped to the keyword arguments defined in the selected macro. This argument should be a YAML string, eg. '{my_variable: my_value}'",
    type=YAML(),
)
