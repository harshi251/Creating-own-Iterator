class TMMissing:pass
class TMRange:
 def __init__(self,start=1,end=TMMissing,step=1):
  if(type(end) is TMMissing)==True:
   end=start
   start=1
  if(type(start)is int)==False:raise TypeError(f"Required {type(33)}, found {type(start)}:{start}")
  if isinstance(end,int)==False:raise TypeError(f"Required {type(33)}, found {type(end)}:{end}")
  if(type(step)is int)==False:raise TypeError(f"Required {type(33)}, found {type(step)}:{step}")
  self.start=start
  self.end=end
  self.current=self.start
  self.step=step
 def __str__(self):
  return f"TMRange({self.start},{self.end})"
 def __iter__(self):
  iterator=TMRangeIterator(self)
  return iterator
class TMRangeIterator:
 def __init__(self,obj):
  self.start=obj.start
  self.end=obj.end
  self.current=obj.current
  self.step=obj.step
 def __str__(self):
  return f"TMRange({self.start},{self.end})"
 def __iter__(self):
  return self;
 def __next__(self):
  if self.start>self.end:
   if self.current<self.end:raise StopIteration
   data=self.current
   self.current+=self.step
   return data
  if self.start<self.end:
   if self.current>self.end:raise StopIteration
   data=self.current
   self.current+=self.step
   return data
   
