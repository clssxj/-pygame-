基于py实现的双人合作的俄罗斯方块游戏，两位玩家在同一个游戏环境中合作，共同消除行数，避免游戏失败。
## 游戏规则：
### 共享游戏区域：

两位玩家共享同一个游戏屏幕区域。每个玩家会有自己的控制块的方式（例如，一个玩家使用键盘的方向键，另一个使用 WASD 键）。玩家需要协调，确保方块能够顺利放置，而不会相互干扰。
### 交换方块：

系统将随机交换下落的方块，以便增加游戏性。此模式强调团队合作和互相帮助。
### 共同得分：

在这种模式下，玩家共享一个分数池，消除的行数和得分会共同计算。成功消除行数可以增加总分，失败时会一起承担游戏的失败。
### 共享失败机制：

如果其中一个玩家失败，整个游戏就结束。这样有利于玩家协作，避免单人失误导致团队失败。

### 得分计算：
每消除一行，玩家的分数增加一分。
应有单独的两行作为计数器，显示分数

## 开发规则
### 速度设定：
游戏速度为每秒 20 帧，每帧 5 毫秒。
开始时，每过十帧帧方块自动下落一格
当游戏分数达到10时，方块速度会加快，每过九帧方块自动下落一格
当游戏分数达到20时，方块速度会加快，每过八帧方块自动下落一格
当游戏分数达到30时，方块速度会加快，每过七帧方块自动下落一格
当游戏分数达到40时，方块速度会加快，每过六帧方块自动下落一格
当游戏分数达到50时，方块速度会加快，每过五帧方块自动下落一格
当游戏分数达到60时，方块速度会加快，每过四帧方块自动下落一格
当游戏分数达到70时，方块速度会加快，每过三帧方块自动下落一格 
当游戏分数达到80时，方块速度会加快，每过两帧方块自动下落一格
当游戏分数大于等于90时，方块速度会加快，每过一帧方块自动下落一格

### 方块设定：
方块选择使用random.choice，保证每次刷新出来的方块不同
用字典映射每种方块
对于每种方块，采取用数组存储其旋转的形状
每次方块固定完之后，依据玩家id重新生成方块

### 边界值设定：
初始化为边界值，即画布大小
当且仅当方块的下部与边界碰撞，方块向上回退一格，并刷新画布，绘制方块，更新边界值

### 输入设定：
玩家分为玩家一和玩家二，分别控制自己的方块
当玩家一按下方向键时，判断方块是否可以移动，并更新方块位置
当玩家二按下 WASD 键时，判断方块是否可以移动，并更新方块位置
方向键上为旋转，方向键下为下降，方向键左为左移，方向键右为右移
w键为旋转，a键为左移，s键为下降，d键为右移
注意判断方块间的碰撞
旋转时以左下角为固定点，重新生成图形


### 碰撞判定：
当方块的下部与边界碰撞，方块向上回退一格
当方块横线碰撞到边界，操作失败
旋转为单独判定，判定周围是否有空间旋转 ，如果按下旋转操作后，与底线值碰撞，则直接将旋转后的图形绘制到画布上，并更新边界值，如果和非底线值之外的边界值碰撞，则无法旋转

### 悬空方块判定：
两个方块都是两个独立的个体，当两个方块碰撞，操作无效

### 游戏结束判定：
方块碰撞到底线值时，判定方块是否超过上界，超过则结束

### 固定方块存储方式：
对于画布内每一行都采取行set的方式存储，当方块固定时，仅需要判定那一行的size是否等于weight即可
当固定方块删除时将上面未消除的set复制下来，并清空复制的行，并使计数器累加分数

### 碰撞判定优先级
悬空方块 < 左右边界值 < 下界