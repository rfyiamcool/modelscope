# Copyright (c) Alibaba, Inc. and its affiliates.
from typing import TYPE_CHECKING

from modelscope.utils.import_utils import LazyImportModule

if TYPE_CHECKING:
    from .retinaface import RetinaFaceDetection
    from .ulfd_slim import UlfdFaceDetector
else:
    _import_structure = {
        'ulfd_slim': ['UlfdFaceDetector'],
        'retinaface': ['RetinaFaceDetection']
    }

    import sys

    sys.modules[__name__] = LazyImportModule(
        __name__,
        globals()['__file__'],
        _import_structure,
        module_spec=__spec__,
        extra_objects={},
    )
