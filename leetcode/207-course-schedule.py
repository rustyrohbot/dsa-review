# 207. Course Schedule
#
# Description:
# There are a total of numCourses courses you have to take, labeled from 0
# to numCourses - 1. You are given an array prerequisites where
# prerequisites[i] = [ai, bi] indicates that you must take course bi first
# if you want to take course ai.
#
# For example, the pair [0, 1] indicates that to take course 0 you have to
# first take course 1.
# Return true if you can finish all courses. Otherwise, return false.
#
# Constraints:
# 1 <= numCourses <= 2000
# 0 <= prerequisites.length <= 5000
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# All the pairs prerequisites[i] are unique.

from typing import List, Dict, Set
import collections

def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    """
    Determines if all courses can be finished given the prerequisites.
    This involves detecting cycles in the course dependency graph.
    """
    # TODO: Implement the solution here
    # Common approaches:
    # 1. Kahn's Algorithm (BFS based on in-degrees)
    # 2. DFS based cycle detection
    pass

if __name__ == "__main__":
    test_cases = [
        {
            "id": "LC Example 1",
            "input": {"numCourses": 2, "prerequisites": [[1, 0]]},
            # 0 -> 1. Possible.
            "expected": True,
        },
        {
            "id": "LC Example 2 (Cycle)",
            "input": {"numCourses": 2, "prerequisites": [[1, 0], [0, 1]]},
            # 0 -> 1 and 1 -> 0. Cycle. Impossible.
            "expected": False,
        },
        {
            "id": "No prerequisites",
            "input": {"numCourses": 3, "prerequisites": []},
            "expected": True,
        },
        {
            "id": "Single course",
            "input": {"numCourses": 1, "prerequisites": []},
            "expected": True,
        },
        {
            "id": "Linear dependencies",
            "input": {"numCourses": 3, "prerequisites": [[1, 0], [2, 1]]},
            # 0 -> 1 -> 2. Possible.
            "expected": True,
        },
        {
            "id": "More complex DAG",
            "input": {
                "numCourses": 4,
                "prerequisites": [[1, 0], [2, 0], [3, 1], [3, 2]],
            },
            #   0 -> 1 \
            #   |      -> 3
            #   -> 2 /
            "expected": True,
        },
        {
            "id": "More complex cycle",
            "input": {
                "numCourses": 3,
                "prerequisites": [[0, 1], [1, 2], [2, 0]],
            },
            # 0 -> 1 -> 2 -> 0. Cycle.
            "expected": False,
        },
        {
            "id": "Disconnected components (still possible)",
            "input": {"numCourses": 4, "prerequisites": [[1, 0], [3, 2]]},
            # 0->1 and 2->3. Possible.
            "expected": True,
        },
        {
            "id": "Self-dependency (cycle)",
            "input": {"numCourses": 2, "prerequisites": [[0, 0]]},
            "expected": False,
        },
        {
            "id": "Multiple paths to a node",
            "input": {"numCourses": 5, "prerequisites": [[0,1],[0,2],[2,3],[3,4]]},
            # 1 -> 0
            # 2 -> 0
            # 3 -> 2
            # 4 -> 3
            # Order: 1, (4->3->2), 0. Or (4->3->2), 1, 0. Possible.
            "expected": True,
        },
         {
            "id": "Long chain with a late cycle",
            "input": {"numCourses": 6, "prerequisites": [[1,0],[2,1],[3,2],[4,3],[5,4],[3,5]]},
            # 0->1->2->3->4->5 and 5->3 (cycle 3-4-5-3)
            "expected": False,
        }
    ]

    passed_all = True
    print("--- Testing LeetCode #207: Course Schedule ---")
    for i, case in enumerate(test_cases):
        num_courses_input = case["input"]["numCourses"]
        prereqs_input = case["input"]["prerequisites"]
        expected_output = case["expected"]
        case_id = case["id"]

        try:
            # Pass copies if the function might modify them, though it shouldn't for this problem.
            actual_output = canFinish(num_courses_input, [list(p) for p in prereqs_input])
            if actual_output == expected_output:
                print(f"Test Case {i + 1} ({case_id}): PASSED")
            else:
                print(f"Test Case {i + 1} ({case_id}): FAILED")
                print(f"  Input numCourses: {num_courses_input}, prereqs: {prereqs_input}")
                print(f"  Expected:         {expected_output}")
                print(f"  Actual:           {actual_output}")
                passed_all = False
        except Exception as e:
            print(f"Test Case {i + 1} ({case_id}): ERROR")
            print(f"  Input numCourses: {num_courses_input}, prereqs: {prereqs_input}")
            print(f"  Exception: {e}")
            import traceback
            traceback.print_exc()
            passed_all = False
        print("-" * 40)

    if passed_all:
        print("All #207 Course Schedule test cases passed!")
    else:
        print("Some #207 Course Schedule test cases failed.")

