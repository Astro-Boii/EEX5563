class MemoryBlock:
    def __init__(self, size):
        self.size = size
        self.is_allocated = False

class WorstFitAllocator:
    def __init__(self, block_sizes):
        self.memory_blocks = [MemoryBlock(size) for size in block_sizes]

    def allocate_memory(self, process_name, process_size):
        worst_index = -1
        worst_size = -1

        # Find the worst fit block
        for i, block in enumerate(self.memory_blocks):
            if not block.is_allocated and block.size >= process_size and block.size > worst_size:
                worst_index = i
                worst_size = block.size

        # Allocate memory if a suitable block is found
        if worst_index != -1:
            block = self.memory_blocks[worst_index]
            block.is_allocated = True
            print(f"Process {process_name} allocated to block of size {block.size}")
            block.size -= process_size  # Update block size after allocation
        else:
            print(f"Process {process_name} could not be allocated (insufficient memory).")

    def free_memory(self, block_index):
        if 0 <= block_index < len(self.memory_blocks):
            block = self.memory_blocks[block_index]
            block.is_allocated = False
            print(f"Block of size {block.size} freed.")
        else:
            print("Invalid block index.")

    def display_memory_state(self):
        print("\nCurrent Memory State:")
        for i, block in enumerate(self.memory_blocks):
            print(f"Block {i}: Size = {block.size}, Allocated = {block.is_allocated}")

if __name__ == "__main__":
    # Initialize memory blocks
    block_sizes = [200, 300, 100, 500, 50]
    allocator = WorstFitAllocator(block_sizes)

    # Display initial memory state
    allocator.display_memory_state()

    # Allocate memory to processes
    allocator.allocate_memory("A", 120)
    allocator.allocate_memory("B", 450)
    allocator.allocate_memory("C", 90)

    # Display memory state after allocation
    allocator.display_memory_state()

    # Free some memory blocks
    allocator.free_memory(3)

    # Display memory state after freeing
    allocator.display_memory_state()