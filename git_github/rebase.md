Git에서 `rebase`는 **기록된 커밋을 새로운 기반(base)으로 재조정**하는 작업입니다. 보통 **브랜치의 커밋을 깔끔하게 정리**하거나, **기존 브랜치를 최신 상태로 업데이트**하기 위해 사용합니다. Rebase는 커밋 히스토리를 한 줄로 이어주는 특성이 있어서, 협업 시 복잡한 merge commit을 줄이는 데 유용합니다.

### Rebase 사용 상황
- **기존 브랜치에 최신 변경 사항을 적용하고 싶은 경우**: 예를 들어, `feature` 브랜치에서 작업 중인데 `main` 브랜치가 업데이트되었다면, `feature` 브랜치도 최신 내용을 반영할 수 있습니다.
- **Merge 커밋을 없애고 깔끔한 히스토리를 만들고 싶을 때**: 여러 기능 브랜치를 `main` 브랜치로 합치면서 불필요한 merge commit을 피하고 싶을 때 사용됩니다.

### 예시 1: `feature` 브랜치에 최신 `main` 반영
1. `feature` 브랜치에서 작업 중인데 `main` 브랜치가 업데이트되었다고 가정합니다.

```bash
# 먼저 main 브랜치로 이동하고 최신 내용을 가져옵니다.
git checkout main
git pull

# 다시 feature 브랜치로 돌아가서 main 브랜치를 rebase 합니다.
git checkout feature
git rebase main
```

이렇게 하면 `feature` 브랜치의 커밋들이 `main`의 최신 상태 위에 재배치됩니다.

### 예시 2: Merge 없이 깔끔한 히스토리 만들기
- `git merge`를 사용하면 히스토리에 "merge commit"이 남습니다. 반면, `git rebase`를 사용하면 **커밋 히스토리가 병합 없이 하나의 직선으로 정리**됩니다.

```bash
# feature 브랜치를 main에 rebase
git checkout feature
git rebase main
```

이 경우, `feature` 브랜치의 커밋들이 `main` 브랜치 끝에 붙어서 히스토리가 단순하게 됩니다.

### 주의사항
- **공유된 브랜치에서는 rebase를 주의**해야 합니다. Rebase는 기존 커밋을 새롭게 만든 커밋으로 교체하기 때문에, 이미 공유된 커밋을 rebase하면 충돌이 발생할 수 있습니다.
- **로컬에서만 작업한 브랜치에 대해 사용**하는 것이 가장 안전합니다.

Rebase는 주로 **히스토리를 깔끔하게 유지**하면서 **병합 과정에서 불필요한 커밋을 줄이기** 위해 유용하게 사용됩니다.
