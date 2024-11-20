"""
Copyright (c) Cutleast
"""

from typing import Callable, Generic, Optional, TypeVar

from PySide6.QtCore import QEventLoop, QThread
from PySide6.QtWidgets import QWidget

T = TypeVar("T")


class Thread(QThread, Generic[T]):
    """
    QThread that optionally blocks the caller thread's execution
    by executing its own event loop while the thread is running.
    """

    __target: Callable[[], T]
    __event_loop: QEventLoop

    __return_result: T = None

    def __init__(
        self,
        target: Callable[[], T],
        name: str | None = None,
        parent: QWidget | None = None,
    ) -> None:
        super().__init__(parent)

        self.__target = target

        if name is not None:
            self.setObjectName(name)

        self.__event_loop = QEventLoop(self)
        self.finished.connect(self.__event_loop.quit)

    def start(self, block: bool = True) -> Optional[T]:
        """
        Starts the thread and waits for it to finish, blocking the execution of MainThread,
        while keeping the Qt application responsive.

        Args:
            block (bool, optional): Blocks the caller thread's execution. Defaults to True.

        Returns:
            The return value of the target function. **None if block is False.**
        """

        super().start()

        if block:
            self.__event_loop.exec()
            return self.__return_result

    def run(self) -> None:
        """
        Runs the target function, storing its return value.

        The return value can be accessed with `start()`.
        """

        try:
            self.__return_result = self.__target()
        except Exception as ex:
            self.__return_result = ex

    def get_result(self) -> T | Exception:
        """
        Returns the return value of the target function.

        Returns:
            The return value or the exception of the target function.
        """

        return self.__return_result
