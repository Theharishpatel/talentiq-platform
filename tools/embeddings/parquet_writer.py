import pyarrow as pa
import pyarrow.parquet as pq

from .config import (
    OUTPUT_FILE,
    COMPRESSION,
)

class EmbeddingWriter:

    def __init__(self):
        
        self.writer = None

    def write(
            self,
            candidate_ids,
            vectors,
    ):
        
        table = pa.Table.from_arrays(

            [
                pa.array(candidate_ids),

                pa.array(vectors.tolist()),
            ],

            names = [
                "candidate_id",
                "embedding",
            ],
        )

        if self.writer is None:

            self.writer = pq.ParquetWriter(

                OUTPUT_FILE,

                table.schema,

                compression=COMPRESSION,
            )

        self.writer.write_table(table)

    def close(self):

        if self.writer:

            self.writer.close()