def topKFrequent(nums: list[int], k: int) -> list[int]:
      hm = {}
      result = []
      for i in range(len(nums)):
          hm[nums[i]] = 1 + hm.get(nums[i], 0)
      
      hm = dict(sorted(hm.items(), key=lambda x: x[1], reverse=True))

      for _ in range(k):
          result.append(max(hm, key=hm.get))
          hm.pop(max(hm, key=hm.get))

      return result
