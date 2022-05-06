"""The baf integration models."""
from __future__ import annotations

import asyncio
from dataclasses import dataclass

from aiobafi6 import Device


@dataclass
class BAFData:
    """Data for the baf integration."""

    device: Device
    run_task: asyncio.Task


@dataclass
class BAFDiscovery:
    """A BAF Discovery."""

    name: str
    ip_address: str
    uuid: str
    model: str
