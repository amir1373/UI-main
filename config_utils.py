"""Configuration helpers for the robot UI."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class RobotEndpoint:
    host: str = "127.0.0.1"
    port: int = 5000
    timeout_s: float = 2.0


def load_json(path: str | Path) -> dict[str, Any]:
    config_path = Path(path)
    if not config_path.exists():
        return {}
    return json.loads(config_path.read_text(encoding="utf-8"))


def load_endpoint(path: str | Path = "config.json") -> RobotEndpoint:
    data = load_json(path)
    robot = data.get("robot", {}) if isinstance(data, dict) else {}
    return RobotEndpoint(
        host=str(robot.get("host", "127.0.0.1")),
        port=int(robot.get("port", 5000)),
        timeout_s=float(robot.get("timeout_s", 2.0)),
    )