{-# LANGUAGE CPP #-}
{-# LANGUAGE NoRebindableSyntax #-}
{-# OPTIONS_GHC -fno-warn-missing-import-lists #-}
{-# OPTIONS_GHC -Wno-missing-safe-haskell-mode #-}
module Paths_x2022_haskell (
    version,
    getBinDir, getLibDir, getDynLibDir, getDataDir, getLibexecDir,
    getDataFileName, getSysconfDir
  ) where

import qualified Control.Exception as Exception
import Data.Version (Version(..))
import System.Environment (getEnv)
import Prelude

#if defined(VERSION_base)

#if MIN_VERSION_base(4,0,0)
catchIO :: IO a -> (Exception.IOException -> IO a) -> IO a
#else
catchIO :: IO a -> (Exception.Exception -> IO a) -> IO a
#endif

#else
catchIO :: IO a -> (Exception.IOException -> IO a) -> IO a
#endif
catchIO = Exception.catch

version :: Version
version = Version [0,1,0,0] []
bindir, libdir, dynlibdir, datadir, libexecdir, sysconfdir :: FilePath

bindir     = "/home/matvs/.cabal/bin"
libdir     = "/home/matvs/.cabal/lib/x86_64-linux-ghc-9.0.2/x2022-haskell-0.1.0.0-inplace-x2022-haskell"
dynlibdir  = "/home/matvs/.cabal/lib/x86_64-linux-ghc-9.0.2"
datadir    = "/home/matvs/.cabal/share/x86_64-linux-ghc-9.0.2/x2022-haskell-0.1.0.0"
libexecdir = "/home/matvs/.cabal/libexec/x86_64-linux-ghc-9.0.2/x2022-haskell-0.1.0.0"
sysconfdir = "/home/matvs/.cabal/etc"

getBinDir, getLibDir, getDynLibDir, getDataDir, getLibexecDir, getSysconfDir :: IO FilePath
getBinDir = catchIO (getEnv "x2022_haskell_bindir") (\_ -> return bindir)
getLibDir = catchIO (getEnv "x2022_haskell_libdir") (\_ -> return libdir)
getDynLibDir = catchIO (getEnv "x2022_haskell_dynlibdir") (\_ -> return dynlibdir)
getDataDir = catchIO (getEnv "x2022_haskell_datadir") (\_ -> return datadir)
getLibexecDir = catchIO (getEnv "x2022_haskell_libexecdir") (\_ -> return libexecdir)
getSysconfDir = catchIO (getEnv "x2022_haskell_sysconfdir") (\_ -> return sysconfdir)

getDataFileName :: FilePath -> IO FilePath
getDataFileName name = do
  dir <- getDataDir
  return (dir ++ "/" ++ name)
